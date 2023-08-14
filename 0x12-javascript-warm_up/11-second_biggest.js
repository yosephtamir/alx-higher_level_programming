#!/usr/bin/node

const arg = Number(process.argv.length);

if (arg > 3) {
  console.log(process.argv.splice(2, process.argv.length - 1).sort().reverse()[1]);
} else {
  console.log(0);
}
