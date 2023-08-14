#!/usr/bin/node

const placeHolder = Number(process.argv[2]);

if (placeHolder) {
  console.log('My number:', placeHolder);
} else {
  console.log('Not a number');
}
