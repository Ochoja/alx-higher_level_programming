#!/usr/bin/node
// Function to return number of occurrences
exports.nbOccurences = function (list, searchElement) {
  let count = 0; //holds number of occurrences

  for (let i of list) {
    if (i === searchElement) {
      count++;
    }
  }

  return count;
}
