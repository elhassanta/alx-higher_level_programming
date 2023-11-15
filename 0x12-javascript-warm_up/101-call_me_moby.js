#!/usr/bin/node
let callMeMoby = function (x, callback) {
  while (x > 0) {
    callback();
    x++;
  };
};
module.exports = callMeMoby;
