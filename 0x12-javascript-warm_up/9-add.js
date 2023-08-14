#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
const addition = add(num1, num2);

console.log(addition);

function add (a, b) {
  return (a + b);
}
