#!/usr/bin/node

const arg = Number(process.argv[2]);

if (arg) {
  let inner = '';
  for (let count = 0; count < arg; count++) {
    for (let count2 = 0; count2 < arg; count2++) {
      inner = inner + 'X';
    }
    if (count < arg - 1) {
      inner = inner + '\n';
    }
  }
  console.log(inner);
} else {
  console.log('Missing size');
}
