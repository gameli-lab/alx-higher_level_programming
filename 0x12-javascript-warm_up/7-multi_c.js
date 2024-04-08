#!/usr/bin/node

const lang = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
const j = process.argv[2];
if (isNaN(j)) { console.log('Missing number of occurrences'); }
while (i < j) {
  console.log(lang[0]);
  i++;
}
