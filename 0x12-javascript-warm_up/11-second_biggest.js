#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let array = process.argv.slice(2);
  array = array.map(Number);
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
