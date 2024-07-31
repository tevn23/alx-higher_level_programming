#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
     console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
});
