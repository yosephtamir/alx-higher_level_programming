#!/usr/bin/node

const args = process.argv;

const length = args.length;

if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
