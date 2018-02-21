
// Create the "p" element for the question
function createChatElement(user, question){
	//Create the elements
	var returnElt = document.createElement("p")
	var usrElt = document.createElement("span");
	var chatElt = document.createElement("span");
	//Get classes for the css
	usrElt.classList.add("usr");
	chatElt.classList.add("chat");
	//Get the value of each element
	usrElt.textContent = user;
	if (user == "Utilisateur : "){
		chatElt.textContent = document.getElementById("question-zone").value;
	} else{
		chatElt.textContent = "Vous m'avez demandé : " + document.getElementById("question-zone").value;
	}
	// Add the "p" elements to the return Element
	returnElt.appendChild(usrElt);	
	returnElt.appendChild(chatElt);
	return returnElt;
}


//Add the content off the "input" in the "chat"
document.getElementById("button").addEventListener("click", function(e){
	// e.preventDefault();
	usrQuestion = createChatElement("Utilisateur : ", );
	question = usrQuestion.getElementsByClassName("chat").value; //store the user question 
	botAnswer = createChatElement("GrandPyBot : ", question);
	document.getElementById("chat").appendChild(usrQuestion);
	document.getElementById("chat").appendChild(botAnswer);
})
