#!/usr/bin/node
exports.esrever = function (list) {
  const leng = list.length - 1;
  const arr = [];
  for (let i = leng; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
