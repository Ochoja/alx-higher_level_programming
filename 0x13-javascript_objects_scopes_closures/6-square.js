#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) { // Print square using the char c
    if (c) {
      let column = `${c}`;

      // Define column
      for (let i = 1; i <= this.width; i++) {
        column += `${c}`;
      }

      // Print rows
      for (let i = 1; i <= this.height; i++) {
        console.log(column);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
