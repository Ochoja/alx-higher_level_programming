#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && !isNaN(w) && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }

    this.print = function () {
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
    };
  }
}

const r1 = new Rectangle(5, 6);
console.log(r1);
