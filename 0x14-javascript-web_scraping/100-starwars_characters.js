#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(url, (error, response, body) => {
  if (!error) {
    const movieInfo = JSON.parse(body);
    movieInfo.characters.forEach(function (character) {
      request(character, (error, response, body) => {
        if (!error) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        }
      });
    });
  }
});
