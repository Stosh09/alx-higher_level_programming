#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

request(url, (error, response, body) => {
  if (!error) {
    let count = 0;
    const information = JSON.parse(body);
    information.results.forEach(function (movie) {
      movie.characters.forEach(function (character) {
        if (character.search('/18/') !== -1) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
