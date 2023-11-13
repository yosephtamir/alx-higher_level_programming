#!/usr/bin/node

const arg = process.argv;

const a = Math.floor(arg[2]);
const b = Math.floor(arg[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(a, b));
