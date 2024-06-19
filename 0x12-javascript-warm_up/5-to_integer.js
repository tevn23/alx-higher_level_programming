#!/usr/bin/node

const arg = process.argv[2];

const argInt = parseInt(arg);

if (!isNaN(argInt)) {
  console.log(`My number: ${argInt}`);
} else {
  console.log('Not a number');
}
