#!/usr/bin/node
exports.esrever = function (list) {
  let revers = [];
  let len = list.length;
  let x = 0;
  while (x < list.length) {
    revers[x] = list[len-1];
    len--;
    x++;
  }
  return revers;
};
