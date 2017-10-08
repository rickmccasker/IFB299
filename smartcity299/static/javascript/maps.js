var map;
var infowindow;

function initMap(latitude, longitude) {
    var location = { lat: latitude, lng: longitude };
    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15
    });
    infowindow = new google.maps.InfoWindow();
    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch({
        location: location,
        radius: 500//,
        //type: ['park']
    }, callback);


    //for loop based on given db array
}

function callback(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    }
}

function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.setContent(place.name);
        infowindow.open(map, this);
    });
}

function createSingleMarker(latitude, longitude, name) {
    alert("ASD");
    var location = { lat: latitude, lng: longitude }
    var marker = new google.maps.Marker({
        map: map,
        position: location
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.setContent(name);
        infowindow.open(map, this);
    });
}

function initMapSingle(latitude, longitude, name) {
    var location = { lat: latitude, lng: longitude };

    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15
    });
    
    infowindow = new google.maps.InfoWindow();
    createSingleMarker(latitude, longitude, name);
    //for loop based on given db array
}