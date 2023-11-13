#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	const x = Number(process.argv[2]);
	let i = 0;
	let str = '';
	while (i < x) {
		str = str + 'X';
		i++;
	}
	i = 0;
	while (i < x) {
		console.log(str);
		i++;
	}
}
