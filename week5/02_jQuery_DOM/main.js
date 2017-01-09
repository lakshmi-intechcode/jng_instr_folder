$(document).ready(function(){

	// var x = document.querySelector('body')
	
	$("body").append("<h1>HELLO WORLD</h1>")
    // $('li#change_me').text('hello, world')

	// var $listItems = $("#list>li"); 

	// $listItems.css("color", "red")
	
	var $add = $('#blah');
	var $addTo = $('#list');

	$add.click(function(){
		console.log("this working")
		var $li = $('<li></li>')
		$li.text("I AM NEW")
		$addTo.append($li)
	})


	// var $z = $('li')
	// console.log($z)
	// $.each($z,(x,y)=>{
	// 	y.addEventListener('click',()=>{
	// 		alert("BLAH")
	// 	})
	// })

	$addTo.click(function(event){
		console.log(event)
		console.log(event.target)
	})


})


// (function start(){ IIFE - Immediately Invoked Function Expression


// }())

// window.onload(){

// }