#!/usr/bin/node
const arg = process.argv;
if (arg[2]) {
	const number = parseInt(arg[2]);
	if (number) {
		console.log(number);
	}
	else
		console.log('Not a number');
} else {
	console.log('Not a number');
}
