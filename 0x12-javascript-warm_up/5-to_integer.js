#!/usr/bin/node
/** Evaluates and print argument if its an integer**/
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
