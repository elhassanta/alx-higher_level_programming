#!/usr/bin/node

let count = 0;
exports.logMe = function (arg) {
  let outer = function (arg) {
    let inner = function () {
      count++;
    }
    console.log(`${count}: ${arg}`);
    inner();
  }
  outer(arg);
};
