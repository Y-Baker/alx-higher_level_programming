#!/usr/bin/node
const SquareLast = require('./5-square');

class Square extends SquareLast {
  charPrint (c = 'X') {
    for (let h = 0; h < this.height; h++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
