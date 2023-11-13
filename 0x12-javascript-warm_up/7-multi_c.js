#!/usr/bin/node

const arg = process.argv;

let count = 0;

if (Math.floor(arg[2])) {
  const length = Math.floor(arg[2]);
  while (count < length) {
    console.log('C is fun');
    count = count + 1;
  }
} else {
  console.log('Missing number of occurrences');
}
