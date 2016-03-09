var map, vector_layer, kml_layer;

$(document).ready(function () {

    // Elements that make up the popup
    var container = document.getElementById('popup');
    var content = document.getElementById('popup-content');
    var closer = document.getElementById('popup-closer');

    //Add a click handler to hide the popup.
    closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
    };

    //Create an overlay to anchor the popup to the map.
    var overlay = new ol.Overlay({
        element: container
    });

    // create bing map layer
    var projection = ol.proj.get('EPSG:3857');

    bing_layer = new ol.layer.Tile({
		source: new ol.source.BingMaps({
			imagerySet: 'AerialWithLabels',
			key: 'SFpNe1Al6IDxInoiI7Ta~LX-BVFN0fbUpmO4hIUm3ZA~AsJ3XqhA_0XVG1SUun4_ibqrBVYJ1XaYJdYUuHGqVCPOM71cx-3FS2FzCJCa2vIh'
		})
	});

    //dcreate kml_layer to show the kml file
	kml_layer = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: "/static/my_first_app/kml/NP_Points.kml",
          format: new ol.format.KML()
        })
      });

    //create vector_layer to show parks established before specific year
    vector_layer = new ol.layer.Vector({
        source: new ol.source.Vector()
    });

    map = new ol.Map({
        layers: [bing_layer, vector_layer, kml_layer],
        overlays: [overlay],
        controls: ol.control.defaults(),
        target: 'map',
        view: new ol.View({
            center: [-11000000, 5500000],
            zoom: 2.5
        })
    });

    //create a slider, when slide, run showparks()
    $( "#slider" ).slider({
        min: 1872,
        max: 2015,
        step: 1,
        slide: function(event, ui) {
            $( "#amount" ).val( ui.value );
            vector_layer.getSource().clear();
            showparks(ui.value);
      }
    });

    $("#amount").val($("#slider").slider("value"));

    //Add a click handler to the map to render the popup.
    map.on('click', function(evt) {
        //Try to get a feature at the point of interest
        var feature = map.forEachFeatureAtPixel(evt.pixel,
            function(feature, layer) {
            return feature;
        });

        //if we found a feature then create and show the popup.
        if (feature) {
            var geometry = feature.getGeometry();
            var coord = geometry.getCoordinates();
            overlay.setPosition(coord);
            var content = document.getElementById('popup-content');
            var displaycontent = feature.get('description');
            content.innerHTML = displaycontent;
        }

        map.getView().setCenter(evt.coordinate);

    })

});

//zoom to selected park
function select_park(){

    kml_layer.setVisible(true);

    var park_dropdown = document.getElementById("select_park").value;
    var myFeature = kml_layer.getSource().getFeatures();

    var feature;
    for (i = 0; i < myFeature.length; i++) {
        feature = myFeature[i];
        if (feature.q.name == park_dropdown) {
            myCoords = feature.getGeometry().getCoordinates();
            map.getView().setCenter(myCoords);
            map.getView().setZoom(9);
            }
        }
    }

//slide event of the slider, add features of parks estabished before selected year to the vector_layer
function showparks(val){

    var year_selected = parseInt(val);

    var myFeature = kml_layer.getSource().getFeatures();

    kml_layer.setVisible(false);

    for(i =0; i < myFeature.length; i++){
         var ymd = myFeature[i].q.description.split("</td>")[6];
         var year = ymd.split("/")[2];
         var year1 = parseInt(year);
             if (year1 <= year_selected) {
                 vector_layer.getSource().addFeature(myFeature[i]);
         }
    }
}


