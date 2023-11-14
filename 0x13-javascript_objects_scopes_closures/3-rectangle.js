#!/usr/bin/node

class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		if (this.width && this.height) {
			let x = 0;
			let str = '';
			while (x < this.width) {
				str = str + 'X';
				x++;
			}
			x = 0;
			while (x < this.height) {
				console.log(str);
				x++;
			}
		}
	}
}

module.exports = Rectangle;

