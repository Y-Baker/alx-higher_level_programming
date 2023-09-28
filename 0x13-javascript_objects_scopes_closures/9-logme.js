#!/usr/bin/node

function cover () {
  let counter = 0;
  return function (item) {
    console.log(counter + ': ' + item);
    counter++;
  };
}

exports.logMe = cover();
