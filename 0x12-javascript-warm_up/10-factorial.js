#!/usr/bin/node

const arg = process.argv;

function factorial (a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

if (Math.floor(arg[2])) {
  console.log(factorial(Math.floor(arg[2])));
} else {
  console.log(1);
}
