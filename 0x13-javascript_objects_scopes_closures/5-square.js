#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (cote) {
	  super(cote, cote);
  }
}
