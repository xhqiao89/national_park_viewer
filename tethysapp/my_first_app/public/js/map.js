var map, kml_layer;

$(document).ready(function () {


    map = new ol.Map({
	layers: [ ],
	controls: ol.control.defaults(),
	target: 'map',
	view: new ol.View({
	    center: [-11000000, 4600000],
		zoom: 3,
        projection: "EPSG:3857"
	})
    });


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


    map.addLayer(bing_layer);
    map.addLayer(kml_layer);

    map.on('click', function(evt) {
        map.getView().setCenter(evt.coordinate);
        map.getView().setZoom(10);
    })

});


