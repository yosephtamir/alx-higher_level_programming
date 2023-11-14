#!/usr/bin/node

let idn = 0;

exports.logMe = function (item) {
  console.log(idn + ': ' + item);
  idn++;
};
