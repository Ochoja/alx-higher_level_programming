#!/usr/bin/node

// Returns reversed version of a list/Array
exports.esrever = function (list) {
  const newArray = [];

  for (const i of list) {
    newArray.unshift(i);
  }

  return newArray;
};
