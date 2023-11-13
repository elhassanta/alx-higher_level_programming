#!/usr/bin/node
const arg = process.argv.length - 2;
if (arg === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[3]);
}
