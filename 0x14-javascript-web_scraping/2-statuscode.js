#!/usr/bin/node

const args = process.argv;
const request = require('request');
const url = args[2];

request(url, (error, response, body) => {
  if (!error) {
    console.log('code: ' + response.statusCode);
  }
});
