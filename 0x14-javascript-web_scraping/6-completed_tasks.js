#!/usr/bin/node
/* Script that computes number
of tasks completed by user id from
https://jsonplaceholder.typicode.com/todos
*/
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);

  const todos = JSON.parse(body);
  const user = {};

  // Loop through todos
  for (const todo of todos) {
    if (todo.completed === true) {
      // increment user's completed task
      if (user[todo.userId]) {
        user[todo.userId]++;
      } else {
        user[todo.userId] = 1;
      }
    }
  }
  console.log(user);
});
