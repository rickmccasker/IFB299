var map;
var infowindow;

/*function initMap(latitude, longitude, query){
    var location = { lat: latitude, lng: longitude };
    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15
    });
    infowindow = new google.maps.InfoWindow();
    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch({
        location: location,
        radius: 500,
        keyword: query
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
}*/

counter = 0;
address = "";

function loadStaticMap() {
    img = document.getElementById("staticMap_img");
    city = document.getElementById("searchCity");
    selected_city = city.options[city.selectedIndex].value;
    img.src = "../media/city/" + selected_city + ".jpg";
    img.onerror = function () {
        alert('error');
        img.src = "../static/images/city404.jpg";
    };
}

function adminMap() {
    var location = { lat: -25.2744, lng: 133.7751 };

    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 4
    });

    var service = new google.maps.places.PlacesService(map);
    var geocoder = new google.maps.Geocoder;

    google.maps.event.addListener(map, 'click', function (event) {
        var request = {
            location: event.latLng,
            radius: '0.1'
        };
        service.nearbySearch(request, checkAmount);
        if (counter >= 1) {
            alert("Location already exists here, please pick another location.")
        } else {
            document.getElementById('Latitude').value = event.latLng.lat();
            document.getElementById('Longitude').value = event.latLng.lng();
            //
            geocoder.geocode({ 'location': event.latLng }, function (results, status) {
                if (status === 'OK') {
                    document.getElementById('Address').value = results[0].formatted_address;
                }
            });
        }
    });
}

function checkAmount(results, status) {
    counter = 0;
    address = "";
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        for (i = 0; i < results.length; i++) {
            if (!results[i].types.includes("locality")) {
                counter += 1;
                alert(results[i].types)
            }
        }
    }
}

function panMap() {
    city = document.getElementById('city').value;
    lat = -25.2744;
    lng = 133.7751;
    if (city == 'SYD') {
        lat = -33.866;
        lng = 151.196;
    } 
    else if (city == "BNE") {
        lat = -27.4698;
        lng = 153.0251;
    }
    else {
        lat = -25.2744;
        lng = 133.7751;
        map.setZoom(4);
        return false;
    }
    map.setCenter(new google.maps.LatLng(lat, lng));
    map.setZoom(15);
    return false;
}


//Single stuff
function createSingleMarker(latitude, longitude, name, address) {
    alert(name);
    var location = { lat: latitude, lng: longitude }
    var marker = new google.maps.Marker({
        map: map,
        position: location
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.setContent(name + "<br>" + address);
        infowindow.open(map, this);
    });
}


//Create an empty map
function initMap(latitude, longitude) {
    var location = { lat: latitude, lng: longitude };

    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15
    });
    
    infowindow = new google.maps.InfoWindow();
}