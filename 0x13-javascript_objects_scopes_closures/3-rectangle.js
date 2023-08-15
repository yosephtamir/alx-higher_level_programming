#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0 && h && w) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let holder = '';
    for (let i = 0; i < Number(this.height); i++) {
      for (let j = 0; j < Number(this.width); j++) {
        holder = holder + 'X';
      }
      if (i < Number(this.height) - 1) {
        holder = holder + '\n';
      }
    }
    console.log(holder);
  }
};
