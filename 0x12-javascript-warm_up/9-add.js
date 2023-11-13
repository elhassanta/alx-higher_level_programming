#!/usr/bin/node
function add(a, b) {
  return a + b;
}

if (process.argv[2] === undefined || process.argv[3] === undefined 
	|| isNaN(process.argv[2]) || isNaN(process.argv[3])) {
	console.log('NaN');
} else {
	console.log(add(process.argv[2], process.argv[3]));
}
