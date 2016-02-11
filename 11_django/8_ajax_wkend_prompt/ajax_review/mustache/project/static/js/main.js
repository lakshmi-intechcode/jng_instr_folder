$(document).ready(function(){

	console.log("We Are Connected");

	$('.movie_form').on('submit', function(event){
		event.preventDefault();
		var movie_title = $('input[name="search_value"]').val();

		$.get({
			url: "search",
			data: {"title": movie_title},
			dataType: "json",
			success: function(data){
				console.log(data)

///////////////////////		First Way		///////////////////////////////

// This will target the element with an id of list
// We use Mustache's "render" function to take the targeted template and load it with the data we got back earlier
// Use jQuery to target the div with the id of "blah" and change the inside of it's html with the variable of the rendered data
				var template = $('#list').html();
				var renderM = Mustache.render(template,data);
				$('#blah').html(renderM)




///////////////////////		Second Way		///////////////////////////////

// This does the same thing as above but we create the template in here
// Mustache just views the template as a string
// We are removing the need for that extra html file holding the template
					// var tpl = "Movies:<ul>{{#Search}}<li>{{Title}} {{Type}}" +
     // 			     "{{Year}}</li>{{/Search}}</ul>";
					// var renderM = Mustache.render(tpl, data)
					// $('#blah').html(renderM)					
			}
		})
	})




///////////////////////		Third Way		///////////////////////////////


// This is just using the jQuery .each method instead of the "#" from Mustache
// Same concept but with jQuery instead of templating. Obviously does not look as clean

				// $.each(moviesRes, function(x){
				// // .html() get the contents of the first element inside #list
				// 	// console.log(moviesRes[x])
				// 	// var template = $('#list').html()

				// 	var el = moviesRes[x]
				// 	console.log(el)
				// 	var tpl = "Movies:<ul>{{#el}}<li>{{el.Title}} {{Type}}" +
    //       "{{Year}}</li>{{/el}}</ul>";
				// 	var renderM = Mustache.render(tpl, el)
				// 	$('#blah').append(renderM)	
				// })

});