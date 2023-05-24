#!/usr/bin/node
/* Store the content of a webpage in a file */
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);

  // Write to file
  fs.writeFile(file, body, err => {
    if (err) return console.log(err);
  });
});
