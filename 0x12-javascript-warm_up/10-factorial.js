#!/usr/bin/node

const arg = Number(process.argv[2]);

const fact = fuc(arg);
console.log(fact);

function fuc (a) {
  if (!a) {
    return 1;
  }

  if (a < 1) {
    return 1;
  } else {
    return a * fuc(a - 1);
  }
}
