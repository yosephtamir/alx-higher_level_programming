#!/usr/bin/node
const fileInput = require('fs');
const req = require('request');
req(process.argv[2]).pipe(fileInput.createWriteStream(process.argv[3]));
