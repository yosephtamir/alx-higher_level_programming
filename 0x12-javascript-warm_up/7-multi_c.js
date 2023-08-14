#!/usr/bin/node

const arg = Number(process.argv[2]);

if (arg) {
  for (let count = 0; count < arg; count++) {
    console.log('C is fun');
  }
}
