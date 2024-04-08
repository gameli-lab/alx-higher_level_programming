#!/usr/bin/node

const { argv } = require('process');
const index = process.argv.length;

if(index < 3)
{
	console.log('No argument');
}
else
{
	console.log(process.argv[2]);
}
