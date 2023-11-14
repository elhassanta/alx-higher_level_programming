#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let occ = 0;
  list.forEach(function (e) {
    if (e === searchElement) {
      occ++;
    }
  });
  return occ;
};
