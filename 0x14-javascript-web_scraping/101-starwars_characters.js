#!/usr/bin/node

/*
const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(char => {
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
*/

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    // Map character URLs to promises that fetch the character data
    const characterPromises = characters.map(charUrl => {
      return new Promise((resolve, reject) => {
        request.get(charUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const charData = JSON.parse(body);
            resolve(charData.name);
          }
        });
      });
    });

    // Wait for all promises to resolve and print character names
    Promise.all(characterPromises)
      .then(charNames => {
        charNames.forEach(charName => {
          console.log(charName);
        });
      })
      .catch(error => {
        console.error(error);
      });
  }
});
