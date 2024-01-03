#!/usr/bin/node
const fs = require('fs');
const content = process.argv[3];
fs.writeFile(process.argv[2], content, 'utf8', function (error, content) {
	if(error) 
	{
		console.log(error);
		return;
	}
	console.log(content);
});
