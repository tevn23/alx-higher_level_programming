#!/usr/bin/node

const args = process.argv.slice(2);

const argInt = parseInt(args[0]);

if (!isNaN(argInt)) {
  for (let i = 0; i < argInt; i++) {
    let row = '';
    for (let j = 0; j < argInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing number of occurrences');
}
