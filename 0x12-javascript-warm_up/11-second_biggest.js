#!/usr/bin/node
/* Searches for second biggest number */
function compareNumbers (a, b) {
  return a - b;
}

if (process.argv[2]) {
  const list = process.argv.slice(2);

  if (list.length <= 1) {
    console.log(0);
  } else {
    list.sort(compareNumbers);
    console.log(list[list.length - 2]);
  }
} else {
  console.log(0);
}
