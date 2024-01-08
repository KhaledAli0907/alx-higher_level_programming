#!/usr/bin/node

function secondBiggest (numbers) {
  if (numbers === undefined) return 0;

  if (numbers.length <= 1) return 0;

  // convert all items in list to numbers
  const intArr = numbers.map(Number);

  // remove dups and sort
  const unique = [...new Set(intArr)].sort((a, b) => b - a);

  //  return seeond elemnt in list
  return unique[1];
}

const args = process.argv.slice(2);

console.log(secondBiggest(args));
