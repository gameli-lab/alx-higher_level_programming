#!/usr/bin/node

const x = process.argv[2];
const y = parseInt(x);
if (isNaN(y)) { console.log('Not a Number'); } else { console.log('My number:', y); }
