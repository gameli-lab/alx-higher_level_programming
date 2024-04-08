#!/usr/bin/node

const { argv } = require('process');

let x = process.argv[2];
let y = parseInt(x);
if (isNaN(y))
	console.log('Not a Number');
else
	console.log('My number:',y);
