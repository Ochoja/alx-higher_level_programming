#!/usr/bin/node
/* Computes and prints factorial */
function factorial (number) {
  if (number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

if (process.argv[2]) {
  console.log(factorial(parseInt(process.argv[2])));
} else {
  console.log(1);
}
