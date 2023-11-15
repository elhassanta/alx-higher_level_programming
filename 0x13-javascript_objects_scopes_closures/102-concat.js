const readFileSync = require('fs').readFileSync;
const writeFile = require('fs').writeFile;
const argv = require('process').argv;

const readFromFile = (file) => {
  return readFileSync(file, 'utf8');
};

const concated = readFromFile(argv[2]) + '' + readFromFile(argv[3]);

writeFile(argv[4], concated, 'utf8', err => {
  if (error) throw error;
});

