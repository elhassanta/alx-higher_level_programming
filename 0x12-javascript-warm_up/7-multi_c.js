#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
	;
} else {
	let count = parseInt(process.argv[2]);
	let i;
	for (i = 0, i < count, i++) {
		console.log('C is fun');
	}
}
