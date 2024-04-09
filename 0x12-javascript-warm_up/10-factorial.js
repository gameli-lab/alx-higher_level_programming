#!/usr/bin/node

function facto (a) {
  if (isNaN(a)) { return (1); } else if ((a === 0) || (a === 1)) { return 1; } else { return (a * facto(a - 1)); }
}
const b = parseInt(process.argv[2]);
console.log(facto(b));
