#!/usr/bin/node

const arg = process.argv;

function factorial (a) {
  let max = a;
  let fact = 1;
  while (max > 0) {
    fact = fact * max;
    max = max - 1;
  }
  return fact;
}

if (Math.floor(arg[2])) {
  console.log(factorial(Math.floor(arg[2])));
} else {
  console.log(1);
}
