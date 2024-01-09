#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // initialize width and height only if they are positive integers
      this.width = w;
      this.height = h;
    } else {
      // if w or h is not a positive integer, create an empty object
      Object.assign(this, {});
    }
  }

  print () {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        console.log('x'.repeat(this.width));
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
