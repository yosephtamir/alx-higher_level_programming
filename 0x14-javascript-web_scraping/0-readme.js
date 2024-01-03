#!/usr/bin/node
const fileInput = require('fs');
fileInput.readFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
