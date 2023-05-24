#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response, body) => {
  if (error) console.log(error);

  const films = JSON.parse(response.body);

  let counter = 0;
  for (const film of films.results) {
    for (const character of film.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        counter++;
      }
    }
  }

  console.log(counter);
});
