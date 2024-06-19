#!/usr/bin/node

const args = process.argv.slice(2);

let i = 0;
const argInt = parseInt(args[0]);

if (!isNaN(argInt)) {
    while (i < argInt) {
        console.log('C is fun');
        i++;
    }
} else {
    console.log('Missing number of occurrences');
}
