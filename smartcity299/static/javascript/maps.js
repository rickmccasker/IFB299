var map;
var infowindow;



counter = 0;
address = "";

/**
Description: 
    Load a static map image, city selected by the "searchCity" field
Parameters: 
    N/A
Return: 
    N/A
**/
function loadStaticMap() {
    img = document.getElementById("staticMap_img");
    city = document.getElementById("searchCity");
    selected_city = city.options[city.selectedIndex].value;
    img.src = "../media/city/" + selected_city + ".jpg";
    img.onerror = function () {
        img.src = "../static/images/city404.jpg";
    };
}

/**
Description: 
    Create a map customised for admin use. Clicking on the map fires an event which will autofill lat,lng and address fields
    to simplify the creation of a place.
Parameters: 
    N/A
Return: 
    N/A
**/
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

/**
Description: 
    Ensure only one result exists at each place.
Parameters: 
    Results - A set of results
    Status - Whether or not the method is able to run based on the place status
Return: 
    N/A
**/
function checkAmount(results, status) {
    counter = 0;
    address = "";
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        for (i = 0; i < results.length; i++) {
            if (!results[i].types.includes("locality")) {
                counter += 1;
            }
        }
    }
}

/**
Description: 
    When relevant button is pressed, pan the map to whereever the city value has been selected.
Parameters: 
    N/A
Return: 
    Boolean - Return false in all cases to prevent submission
**/
function panMap() {
    city = document.getElementById('city').value;
    lat = -25.2744;
    lng = 133.7751;
    if (city == 'Sydney') {
        lat = -33.865143;
        lng = 151.209900;
    } 
    else if (city == "Brisbane") {
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


/**
Description: 
    Create a single marker on a map with the given params.
Parameters: 
    Latitude - The latitude of the pin
    Longitude - The longitude of the pin
    Name - The name of the pin, to be used in its infobox
    Address - The address of the pin, to be used in its infobox
Return: 
    N/A
**/
function createSingleMarker(latitude, longitude, name, address) {
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


/**
Description: 
    Initialise an empty map, ready to be filled
Parameters: 
    Latitude, Longitude - Where the map should be centered around
Return: 
    N/A
**/
function initMap(latitude, longitude) {
    var location = { lat: latitude, lng: longitude };

    map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15
    });
    
    infowindow = new google.maps.InfoWindow();
}