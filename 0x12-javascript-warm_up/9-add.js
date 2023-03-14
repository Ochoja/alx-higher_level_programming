#!/usr/bin/node
/* Prints addition of 2 integers */
function add(a, b) {
  return parseInt(a) + parseInt(b);
}

if (process.argv[2] && process.argv[3]) {
  console.log(add(process.argv[2], process.argv[3]));
} else {
  console.log(NaN)
}
