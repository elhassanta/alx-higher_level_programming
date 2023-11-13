#!/usr/bin/node
const arg = process.argv.length - 1;
if (arg === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
