#!/usr/bin/node

const Rectangel = require('./4-rectangle');
class Square extends Rectangle {
  constructor (cote) {
	  super(cote, cote);
  }
}
