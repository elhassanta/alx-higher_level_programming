#!/usr/bin/node
const arg = process.argv;
if (!arg[3]) {
  console.log('No argument');
} else {
  console.log(process.argv[3]);
}
