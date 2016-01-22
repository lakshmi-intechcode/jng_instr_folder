$(document).ready(function(){

	// $("button").on("click", function(){
	// 	console.log($(this))
	// })

	// console.log(this)

	// var myThis = function(x){
	// 	console.log(this)
	// }

	// $("button").on("click", myThis)

	var Car = function(make, model, color, year){
		this.make = make;
		this.model = model;
		this.color = color;
		this.year = year
	};

	var bugatti = new Car("Bugatti", "Veyron", "red", 2013)

	console.log(bugatti)
	console.log(bugatti.color)
});