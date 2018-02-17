//Add the content off the "input" in the "chat"
document.getElementById("button").addEventListener("click", function(e){
	var chatElt = document.createElement("p");
	var usrText = document.createElement("span")
	usrText.classList.add("usr");
	usrText.textContent = "Utilisateur : ";
	chatElt.appendChild(usrText);
	chatElt.appendChild(document.createTextNode(document.getElementById("question-zone").value));
	document.getElementById("chat").appendChild(chatElt);
})