#!/usr/bin/node

const arg = process.argv;
const length = arg.length;
let spaceh;
let count = 2;
let spacei;
if (length < 4) {
  console.log(0);
} else if (length > 2) {
  spaceh = arg[2];
  spacei = arg[2];
  while (count < length) {
    if (spaceh < arg[count]) {
      spacei = spaceh;
      spaceh = arg[count];
    }
    count = count + 1;
  }
  console.log(spacei);
}
