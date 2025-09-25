#!/usr/bin/node

const languages = [
  'C is fun',
  'Python is cool',
  'Javascript is amazing'
];

let result = '';

for (const index in languages) {
  result += languages[index] + '\n';
}

console.log(result.trim());
