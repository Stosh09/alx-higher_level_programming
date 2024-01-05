#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(url, (error, response, body) => {
  if (!error) {
    const information = JSON.parse(body);
    console.log(information.title);
  }
});
