#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

const filename = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
