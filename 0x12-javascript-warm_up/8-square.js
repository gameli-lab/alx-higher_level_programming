#!/usr/bin/node

let i, j, row;
const size = process.argv[2];
if (isNaN(size)) { console.log('Missing size'); }
for (i = 0; i < size; i++) {
  row = '';
  for (j = 0; j < size; j++) { row += 'X'; }
  console.log(row);
}
