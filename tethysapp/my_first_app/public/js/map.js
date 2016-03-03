var map, vector_layer, kml_layer;

$(document).ready(function () {

    var container = document.getElementById('popup');
    var content = document.getElementById('popup-content');
    var closer = document.getElementById('popup-closer');

    closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
    };
    var overlay = new ol.Overlay({
        element: container
    });

    var projection = ol.proj.get('EPSG:3857');

    bing_layer = new ol.layer.Tile({
		source: new ol.source.BingMaps({
			imagerySet: 'AerialWithLabels',
			key: 'SFpNe1Al6IDxInoiI7Ta~LX-BVFN0fbUpmO4hIUm3ZA~AsJ3XqhA_0XVG1SUun4_ibqrBVYJ1XaYJdYUuHGqVCPOM71cx-3FS2FzCJCa2vIh'
		})
	});

	kml_layer = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: "/static/my_first_app/kml/NP_Points.kml",
          format: new ol.format.KML()
        })
      });

    vector_layer = new ol.layer.Vector({
        source: new ol.source.Vector(),
        style: new ol.style.Style({
            fill: new ol.style.Fill({
                color: 'rgba(255, 255, 255, 0.2)'
            }),
            stroke: new ol.style.Stroke({
                color: '#ffcc33',
                width: 10
            }),
            image: new ol.style.Circle({
                radius: 40,
                fill: new ol.style.Fill({
                    color: '#ffcc33'
                })
            })
        })
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

    $( "#slider" ).slider({
        min: 1872,
        max: 2015,
        step: 10,
        change: function(event, ui) {
            $( "#amount" ).val( ui.value );
            vector_layer.getSource().clear();
            showparks(ui.value);
      }
    });

    $("#amount").val($("#slider").slider("value"));

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

function select_park(){

    var park_dropdown = document.getElementById("select_park").value;
    var myFeature = kml_layer.getSource().getFeatures();

    var feature;
    for (i = 0; i < myFeature.length; i++) {
        feature = myFeature[i];
        if (feature.q.name == park_dropdown) {
            myCoords = feature.getGeometry().getCoordinates();
            map.getView().setCenter(myCoords);
            map.getView().setZoom(10);
            map.getOverlays().item(0).setPosition(myCoords);
            }
        }
    }


function showparks(val){

    var year_selected = parseInt(val);

    kml_layer.setVisible(false);

    var myFeature = kml_layer.getSource().getFeatures();

    for(i =0; i < myFeature.length; i++){
         var ymd = myFeature[i].q.description.split("</td>")[6];
         var year = ymd.split("/")[2];
         var year1 = parseInt(year);
             if (year1 < year_selected) {
                 vector_layer.getSource().addFeature(myFeature[i]);
         }
    }
}


