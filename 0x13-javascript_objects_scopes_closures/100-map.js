#!/usr/bin/node

const main = require('./100-data').list;

console.log(main);
console.log(main.map((x, idx) => x * idx));
