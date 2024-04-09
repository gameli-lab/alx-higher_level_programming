#!/usr/bin/node

function slarge (arr) {
  if (arr.length <= 1) { return 0; } else { arr.sort((a, b) => b - a); }
  return arr[1];
}
const x = process.argv.slice(2).map(Number);
console.log(slarge(x));
