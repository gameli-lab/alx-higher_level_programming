#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
	if (error) {
		console.error('Error:', error);
	} else {
		console.log('Code:', response.statusCode);
	}
});