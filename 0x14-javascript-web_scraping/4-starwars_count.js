#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).results;
    const films = data.filter(film => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(films.length);
  }
});
