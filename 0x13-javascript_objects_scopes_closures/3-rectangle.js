#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      this.width = ;
      this.height = ;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
