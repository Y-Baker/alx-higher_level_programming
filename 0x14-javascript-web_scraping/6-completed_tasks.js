#!/usr/bin/node

const request = require('request');

apiUrl = process.argv[2];
request(apiUrl, (err, res, body) => {
  console.log('here');
  if (!err && res.statusCode === 200) {
    const dict = {};
    body = JSON.parse(body);
    for (const task of body) {
      if (task.completed == true) {
        if (dict[task.userId]) dict[task.userId]++;
        else dict[task.userId] = 1;
      }
    }
    console.log(dict);
  }
});
