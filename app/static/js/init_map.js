// GOOGLE MAPS SETUP: Javascript API //

// Gmap elements
var map = {};
var marker = {};
var infowindow = {};

// Function called when page has been loaded
function initMap() {
    
    coordinates = {lat: 48.856614, lng: 2.3522219} // initial coord displayed on the page
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coordinates,
        mapTypeId: google.maps.MapTypeId.ROADMAP

        
    });
    
    marker = new google.maps.Marker({
        position: coordinates,
        map: map
    });
   
   infowindow = new google.maps.InfoWindow(); 
}


// function called to actualise map with new coordiantes
function actualise_map(latitude, longitude, address) {
  
  
  infowindow.setContent(address);
  coordinates = {lat: latitude, lng: longitude};
  map.panTo(coordinates);
  marker.addListener('position_changed', function() {
    infowindow.close();
    infowindow.open(map, marker);
  })
  marker.setPosition(coordinates);
  marker.setAnimation(google.maps.Animation.BOUNCE);

  marker.addListener('click', function() {
          
          infowindow.open(map, marker);
        });


  map.setZoom(15)

}