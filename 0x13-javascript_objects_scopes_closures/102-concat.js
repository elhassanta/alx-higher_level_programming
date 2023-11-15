#!/usr/bin/node
const readFileSync = require('fs').readFileSync;
const writeFile = require('fs').writeFile;
const argv = require('process').argv;
const getContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concated = getContent(argv[2]) + '' + getContent(argv[3]);

writeFile(argv[4], concated, 'utf8', err => {
  if (err) throw err;
});
