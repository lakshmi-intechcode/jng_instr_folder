var header = document.getElementById("myHeader")

var namedFunc= function(){
	alert("Does this work?")
}

header.addEventListener("click", namedFunc);

// header.addEventListener("click", function(){
// 	alert("Does this work?")
// })