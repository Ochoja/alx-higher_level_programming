#!/usr/bin/node

global.globalCount = 0;

// Function prints the number of arguments
// already printed and the new argument value
exports.logMe = function (item) {
  console.log(`${globalCount}: ${item}`);
  globalCount++;
};
