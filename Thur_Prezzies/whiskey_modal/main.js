$(".open-modal").on("click", function() {
  console.log(this.id)
  // blantons()
  modal_func(this.id)
});

$("#close").on("click", function() {
  $(".modal").toggle();
});

var modal_func = function(w){
	console.log(whiskeys[w])
	var heading = whiskeys[w].heading;
	var describe = whiskeys[w].describe;
	var image = whiskeys[w].image;

	$(".heading").html(heading);
  $(".describe").html(describe)
  $("img").attr("src", image)
  $(".modal").toggle();
}
