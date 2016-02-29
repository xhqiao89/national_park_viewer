var map, kml_layer;

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

	var kml_layer = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: "/static/my_first_app/kml/NP_Points.kml",
          format: new ol.format.KML()
        })
      });

    //map.addLayer(bing_layer);
    //map.addLayer(kml_layer);

    map = new ol.Map({
        layers: [bing_layer, kml_layer],
        overlays: [overlay],
        controls: ol.control.defaults(),
        target: 'map',
        view: new ol.View({
            center: [-11000000, 5500000],
            zoom: 2.5,
        })
    });


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
        var displaycontent = feature.get('description');
        content.innerHTML = displaycontent;
    }

        map.getView().setCenter(evt.coordinate);
        //map.getView().setZoom(5);
    })

});

function select_state(){
    dropdown_obj=document.getElementById("select_state");

}


