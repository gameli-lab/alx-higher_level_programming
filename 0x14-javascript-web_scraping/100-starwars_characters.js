#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach(char => {
      request.get(char, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    });
  }
});
