(function start(){ //WRAP SHIT IN IIFE
	
//characters
	var jedi = [
		"Luke Skywalker",
		"Obi Wan Kenobi"
	];
	var millenium = [
		"Han Solo",
		"Chewbacca"
	];
	var royalty = "Leia Organa";
	var darkside = "Darth Vader";

//combine characters for falcon
	var heroes = 

//Values for Control Flow with click events
	var time = "arrive";
	var escape = false;

	///////////////////////// Making Your Story /////////////////////////

//target the different DOM elements
	var tatooine = 
	var falcon = 
	var deathStar = 
	var xwing = 

	var findLuke = function(){
		// Make divs that will have the text in the jedi array
		// One div for obi wan and one for luke
		// These divs will have a class called jedi
		// These divs should be appended to tatooine
	};

	var leaveTatooine = function(){
		// Remove Obi Wan and Luke from Tatooine
		// Put Obi Wan, Luke, Han, and Chewy on the Millenium Falcon
		// This will be easier if you combine these two groups using the already defined "heroes" variable up top
		// Give each hero element their own div
		// Give all the newly created divs a class called "heroes"
		// Append all the new heroes divs to the Millenium Falcon
	};

	var findLeia = function(){
		// Remove all characters from the falcon
		// Put them on the Death Star
		// Put Leia on the death Star
		// Leia is in her own variable right now, how can we put her with the other heroes?
		// Give all the heroes their own div elements
		// Append the hero divs to the death star
	};

	var vaderAndObi = function(){
		// OH MAN DARTH VADER HAS APPEARED
		//append vader to the death star
		//remove Obi Wan Kenobi

		var good = document.getElementsByClassName("heroes");

		for (var i = 0; i<good.length; i++){
			if (good[i].innerHTML === "Obi Wan Kenobi"){
				deathStar.removeChild(good[i])
				var div = document.createElement("div");
				div.setAttribute("class", "vader");
				div.innerHTML = darkside;
				deathStar.appendChild(div);

				//Remove Obi Way from Heroes Array
				var ind = heroes.indexOf("Obi Wan Kenobi");
				heroes.splice(ind, 1);
			}; 
		};
	};

	var retreat = function(){
		//delete the heroes from death star
		//add heroes to falcon

		var good = document.getElementsByClassName("heroes");
		var party = good.length;

		for (var i=0; i<party; i++){
			deathStar.removeChild(good[0]);
		};

		for(var i=0; i<heroes.length; i++){
			var div = document.createElement("div");
			div.innerHTML = heroes[i];
			div.setAttribute("class", "heroes");
			falcon.appendChild(div);
		}
	};

	var battle = function(){
		//Delete Leia from the falcon element
		//Delete Leia from the heroes list
		//Delete Luke from falcon
		//Append Luke to X-wing

		var depart = document.getElementsByClassName("heroes");

		for(var i=0; i<depart.length; i++){
			if (depart[i].innerHTML === "Luke Skywalker" || depart[i].innerHTML === "Leia Organa"){
				falcon.removeChild(depart[i]);
				i-=1
			};
		};

		var div = document.createElement("div");
		div.innerHTML = "Luke Skywalker";
		xwing.appendChild(div);
		deathStar.remove()

	};


////////////////////////////// CLICK EVENTS /////////////////////////////
	tatooine.addEventListener('click', findLuke);
	falcon.addEventListener('click', function(){
		if (escape === true){
			retreat();
		} else {
			leaveTatooine();
		};
	});
	deathStar.addEventListener("click", function(){
		if (time === "arrive"){
			findLeia();
			time = "depart";
		} else if (time === "depart"){
			vaderAndObi();
			escape = true;
		};
	});
	xwing.addEventListener("click", battle);


}())//END OF IIFE



