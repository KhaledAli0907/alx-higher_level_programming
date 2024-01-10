#!/usr/bin/node

class rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // initialize width and height only if they are positive integers
      this.width = w;
      this.height = h;
    } else {
      // if w or h is not a positive integer, create an empty object
      object.assign(this, {});
    }
  }

  print() {
	for (let row = 0; row < this.height; row++) {
		console.log('X'.repeat(this.width));
	}
  }
}
module.exports = rectangle;
