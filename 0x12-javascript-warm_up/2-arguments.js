#!/usr/bin/node

const args = process.argv;
console.log(args);
if (args.length > 3) {
  console.log('Arguments found');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
