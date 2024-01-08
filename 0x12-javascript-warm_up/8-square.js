#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2])) process.exit(1, console.log('Missing size'));

for (let row = 0; row < Number(argv[2]); row++) {
  console.log('X'.repeat(Number(argv[2])));
}
