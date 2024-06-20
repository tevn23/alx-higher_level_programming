#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log('0');
} else {
  const num = args.map(arg => parseInt(arg)).sort((a, b) => b - a);

  const uniqueNum = [...new Set(num)];

  if (uniqueNum.length < 2) {
    console.log('0');
  } else {
    console.log(uniqueNum[1]);
  }
}
