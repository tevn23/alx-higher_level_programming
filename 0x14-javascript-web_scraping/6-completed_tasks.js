#!/usr/bin/env node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });

  console.log(completedTasks);
});
