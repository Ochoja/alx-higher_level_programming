#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);

  const films = JSON.parse(response.body);

  let counter = 0;
  for (const film of films.results) {
    for (const character of film.characters) {
      if (character.includes('/18/')) {
        counter++;
      }
    }
  }

  console.log(counter);
});
