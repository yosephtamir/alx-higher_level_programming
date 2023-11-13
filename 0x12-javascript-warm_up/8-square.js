#!/usr/bin/node

const arg = process.argv;
let sum = '';
let count = 0;
let countIn;

if (Math.floor(arg[2])) {
  const length = Math.floor(arg[2]);
  while (count < length) {
    countIn = 0;
    while (countIn < length) {
      sum = sum + 'X';
      countIn = countIn + 1;
    }
    if (count < length - 1) {
      sum = sum + '\n';
    }
    count = count + 1;
  }
  console.log(sum);
} else {
  console.log('Missing size');
}
