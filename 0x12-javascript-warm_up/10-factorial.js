#!/usr/bin/node

function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 1 || isNaN(n)) {
    return (1);
  }
  return (factorial(n - 1) * n);
}

console.log(factorial(Number(process.argv[2])));
