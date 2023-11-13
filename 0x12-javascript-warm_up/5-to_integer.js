#!/usr/bin/node

const arg = process.argv;

if (Math.floor(arg[2])) {
  console.log('My number: ' + Math.floor(arg[2]));
} else {
  console.log('Not a number');
}
