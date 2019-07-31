'use strict';

// Setup socket.io-client
const io = require('socket.io-client');
const cron = require('node-cron');

// connect to server.js
const socket = io.connect('http://localhost:3006');

// let count = 30;

let data = {
  moistureNumber: 500,
  timeStamp: new Date(),
}

// while (count) {
//   setTimeout(() => {
//     socket.emit('moisture-data', JSON.stringify(data));
//     count--;
//   }, 1000)
// }

cron.schedule('*/2 * * * * *', function() {
  console.log('hello');
  socket.emit('moisture-data', JSON.stringify(data));
});

