// function initMap(lat_search, lng_search, place) {
//         var uluru = {lat: lat_search, lng: lng_search};
//         var map = new google.maps.Map(document.getElementById('map'), {
//           zoom: 4,
//           center: place
//         });
//         var marker = new google.maps.Marker({
//           position: place,
//           map: map
//         });
//       }


// function initMap() {
//         var uluru = {lat: 47.23184999999999, lng: -1.5584598};
//         var map = new google.maps.Map(document.getElementById('map'), {
//           zoom: ,
//           center: nantes
//         });
//         var marker = new google.maps.Marker({
//           position: nantes,
//           map: map
//         });
//       }

function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }