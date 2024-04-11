#!/usr/bin/node

exports.logMe = function (item) {
  if (!this.count) { this.count = 0; }
  this.count++;
  console.log(`${this.count}:${item}`);
};
