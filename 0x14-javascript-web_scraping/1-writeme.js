#!/usr/bin/node
const fileInput = require('fs');
fileInput.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
