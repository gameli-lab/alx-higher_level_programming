#!/usr/bin/node

const { argv } = require('process');
const index = process.argv.length;

if(index < 3)
{
	console.log('No argument');
}
else if(index === 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
