
//Function to add elements in the chat
function addChatElement(user,chat){
	//Create the elements
	var returnElt = document.createElement("p")
	var usrElt = document.createElement("span");
	var chatElt = document.createElement("span");
	//Get classes for the css
	usrElt.classList.add("usr");
	chatElt.classList.add("chat");
	//Get the value of each element
	usrElt.textContent = user;
	chatElt.textContent = chat;
	// Add the "p" elements to the return Element
	returnElt.appendChild(usrElt);	
	returnElt.appendChild(chatElt);
	return returnElt;
}

//Function to display the map from google
function initMap(lat, long) {
    var place = {lat: lat, lng: long};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: place
    });
    var marker = new google.maps.Marker({
      position: place,
      map: map
    });
  }


//Add asynchronous request to wiki api
$(function(){
	var submit_form = function(e){
		$.getJSON($SCRIPT_ROOT + '/wiki_api', {keywords: $('input[name="question"]').val()}, function(data){
			$('#chat').append(addChatElement('Utilisateur : ', $('input[name="question"]').val()));
			$('#chat').append(addChatElement('GrandPyBot : ', data));
		});
	return false;
	};
	$('#button').on('click', submit_form);
});

//Add asynchronous request to google api
$(function(){
	var submit_form = function(e){
		$.getJSON($SCRIPT_ROOT + '/google_api', {keywords: $('input[name="question"]').val()}, function(data){
			var map = document.createElement("div");
			map.id = "map";
			map.classList.add("col-md-offset-1");
			map.classList.add("col-md-10");
			$('#chat').append(map);
			var lat = Number(data[0]);
			var long = Number(data[1]);
			initMap(lat, long);
		});
	return false;
	};
	$('#button').on('click', submit_form);
});
