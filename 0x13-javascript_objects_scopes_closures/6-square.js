#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint(c) {
    if (c) {
      let x = 0;
      let str = '';
      while (x < this.width) {
        str = str + c;
        x++;
      }
      x = 0;
      while (x < this.height) {
        console.log(str);
        x++;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
