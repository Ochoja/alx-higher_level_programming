#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && !isNaN(w) && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let column = '';

      // Create column
      for (let i = 1; i <= this.width; i++) {
        column += 'X';
      }

      // Print rows
      for (let i = 1; i <= this.height; i++) {
        console.log(column);
      }
    }
  }

  // Exchanges the width and height
  rotate () {
    const hold = this.width;
    this.width = this.height;
    this.height = hold;
  }

  // Doubles the width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
