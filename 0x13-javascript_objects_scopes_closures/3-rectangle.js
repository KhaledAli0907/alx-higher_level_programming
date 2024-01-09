#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // Initialize width and height only if they are positive integers
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      Object.assign(this, {});
    }
  }

  print() {
	for (let row = 0; row < this.height; row++) {
		console.log('X'.repeat(this.width));
	}
  }
}
module.exports = Rectangle;
