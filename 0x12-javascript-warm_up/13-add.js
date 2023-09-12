#!/usr/bin/node

const newFun = function (a, b) {
  return (a + b);
};

exports.add = newFun;
