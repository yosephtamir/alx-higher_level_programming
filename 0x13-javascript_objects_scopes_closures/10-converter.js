#!/usr/bin/node

exports.converter = function (base) {
  function Convert (n) {
    return n.toString(base);
  }

  return Convert;
};
