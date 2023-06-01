#!/usr/bin/node
/* Display status code of request */
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log(`code: ${response.statusCode}`);
});