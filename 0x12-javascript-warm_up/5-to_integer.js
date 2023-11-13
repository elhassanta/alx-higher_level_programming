#!/usr/bin/node
const arg = process.argv;
if (arg[2]) {
	const number = parseInt(arg[2]);
	if (isNaN(number) || number === undefined) {
		console.log('Not a number');
	}
	else {
		console.log('My number: ' ,number);
	}
} else {
	console.log('Not a number');
}
