#!/usr/bin/node
const quer = require('request');
quer.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
