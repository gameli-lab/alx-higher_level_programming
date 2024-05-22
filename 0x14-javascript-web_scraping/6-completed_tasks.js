#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const completeTasks = data.filter(task => task.completed === true);
    const result = {};
    completeTasks.forEach(task => {
      if (result[task.userId]) {
        result[task.userId]++;
      } else {
        result[task.userId] = 1;
      }
    });
    console.log(result);
  }
});
