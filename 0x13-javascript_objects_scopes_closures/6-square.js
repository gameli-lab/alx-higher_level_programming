#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) { this.print(); return; }
    for (let x = 0; x < this.size; x++) {
      let row = '';
      for (let y = 0; y < this.size; y++) {
        row += c;
      }
      console.log(row);
    }
  }
};
