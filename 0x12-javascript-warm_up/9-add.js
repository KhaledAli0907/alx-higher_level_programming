#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2]) || isNaN(argv[3])) {
  process.exit(1, console.log('Nan'));
}

function add (a, b) {
  return (Number(a) + Number(b));
}

console.log(add(Number(argv[2]), Number(argv[3])));
