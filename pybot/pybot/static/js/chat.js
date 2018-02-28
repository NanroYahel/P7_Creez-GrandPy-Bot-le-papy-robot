
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


//Add asynchronous request to wiki api
$(function(){
	var submit_form = function(e){
		$.getJSON($SCRIPT_ROOT + '/wiki_api', {keywords: $('input[name="question"]').val()}, function(data){
			$('#chat').append(addChatElement('Utilisateur : ', $('input[name="question"]').val()));
			$('#chat').append(addChatElement('GrandPyBot : ', data));
			// $('span.bot_chat').text(data);
		});
	return false;
	};
	$('#button').on('click', submit_form);
});

