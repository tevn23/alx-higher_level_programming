#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const num = parseInt(args[0]);

const result = factorial(num);

console.log(result);
