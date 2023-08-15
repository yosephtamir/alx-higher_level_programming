#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let holder = '';
    let place = 'X';
    if (c) {
      place = c;
    }
    for (let i = 0; i < Number(this.height); i++) {
      for (let j = 0; j < Number(this.width); j++) {
        holder = holder + place;
      }
      if (i < Number(this.height) - 1) {
        holder = holder + '\n';
      }
    }
    console.log(holder);
  }
};
