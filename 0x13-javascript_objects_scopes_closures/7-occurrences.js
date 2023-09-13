#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const ele of list) {
    if (ele === searchElement) {
      counter++;
    }
  }

  return (counter);
};
