#!/usr/bin/node
/* Script that prints a square */
if (!isNaN(process.argv[2])) {
  let text = '';
  for (let i = 0; i < process.argv[2]; i++) {
    text += 'X';
  }

  for (let i = 0; i < process.argv[2]; i++) {
    console.log(text);
  }
} else {
  console.log('Missing size');
}
