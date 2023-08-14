#!/usr/bin/node

const arg = process.argv.length;

if (arg > 3) {
  const innerarg = Number(process.argv.splice(2, process.argv.length - 1).sort().reverse()[1]);
  if (innerarg) {
    console.log(innerarg);
  } else {
    console.log(innerarg);
  }
} else {
  console.log(0);
}
