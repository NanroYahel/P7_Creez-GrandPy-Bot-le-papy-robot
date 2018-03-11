//List of sentences for the answer of pybot
var randomSentences = ['C\'est intéressant ! Je suis sûr que tu ne sais même pas que : ', 'Très bon choix ! D\'ailleurs, savais-tu que : ', 'J\'adore cet endroit. Je ne sais pas si tu sais mais : ' ]

//Get random setence from the list above
function getRandomSentence(){
	var randomNumber = Math.floor(Math.random() * (3 - 1)) + 0;
	var sentence = randomSentences[randomNumber];
	return sentence;
}

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

//Display the question of the user
$('#button').on('click', function(){
	$('#chat').append(addChatElement('Utilisateur : ', $('input[name="question"]').val()));
});

//Add asynchronous request to google api
$(function(){
	var submit_form = function(e){
		$.getJSON($SCRIPT_ROOT + '/google_api', {keywords: $('input[name="question"]').val()}, function(data){
			if (data === 'NORETURN'){
				$('#chat').append(addChatElement('GrandPyBot : ', "Je ne comprends pas ce que tu cherches..."))
			} else{
			var lat = Number(data[0]);
			var long = Number(data[1]);
			var address = data[2];
			if (address != ''){
				$('#chat').append(addChatElement('GrandPyBot : ', 'Le lieu que tu cherches se situe : ' + address + '.'))
			}
			initMap(lat, long);
			}
		});
	return false;
	};
	$('#button').on('click', submit_form);
});

//Add asynchronous request to wiki api
$(function(){
	var submit_form = function(e){
		$.getJSON($SCRIPT_ROOT + '/wiki_api', {keywords: $('input[name="question"]').val()}, function(data){
			$('#chat').append(addChatElement('GrandPyBot : ', getRandomSentence() + '"' + data + '"'));
		});
	return false;
	};
	$('#button').on('click', submit_form);
});


//Initialize chat with a welcome message
var welcomeMessage = "Bonjour jeune curieux ! Où souhaites-tu te rendre ? ";
$('#chat').append(addChatElement('GrandPyBot : ', welcomeMessage));


