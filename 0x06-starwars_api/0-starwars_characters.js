#!/usr/bin/node
// Star Wars API

const request = require('request');

function fetchCharacters (filmId) {
  const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  request(url, async function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    const film = JSON.parse(body);
    for (const characterUrl of film.characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
            return;
          }
          const character = JSON.parse(body);
          console.log(character.name);
          resolve();
        });
      });
    }
  });
}

// Extracting Film ID from command line arguments
const filmId = process.argv[2];

// Check if Film ID is provided
if (filmId) {
  fetchCharacters(filmId);
} else {
  console.log('Please provide the Movie ID as a command line argument.');
}
