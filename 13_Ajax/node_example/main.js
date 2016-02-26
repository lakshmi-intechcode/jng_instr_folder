var fs = require('fs');

fs.readFile('Forty-One_Thieves.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading Forty-One_Thieves, Asynchronously...")
});

fs.readFile('The_Legends_Of_King_Arthur_And_His_Knights.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading King Arthur, Asynchronously...")
});


fs.readFile('The_Sense_Of_Wonder.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading The_Sense_Of_Wonder, Asynchronously...")
});

console.log("FINISHED ALL THE BOOKS")




