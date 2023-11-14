#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach(function (e) {
    if (e === searchElement) {
      occ++;
    }
  });
  return occ;
};
