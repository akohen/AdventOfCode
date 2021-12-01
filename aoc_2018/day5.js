fs = require('fs');

function day5(str) {
  let c = 0;
  while( c < str.length) {
    if(Math.abs(str.charCodeAt(c) - str.charCodeAt(c+1)) === 32) {
      str = str.slice(0, c) + str.slice(c+2, str.length);
      c--
    } else {
      c++
    }
  }
  return str.length
}

function removeChar(input, charCode) {
  let res = '';
  for (let i = 0; i < input.length; i++) {
    if( !(input.charCodeAt(i) == charCode || input.charCodeAt(i) == charCode + 32) )
      res += input[i]
  }
  return res
}

function step2(input) {
  let shortest = 9999999
  for(let i=65; i<92; i++) {
    shortest = Math.min(shortest, day5(removeChar(input, i)))
  }
  return shortest
}

fs.readFile('input/day5','utf-8', (err, data) => { console.log(day5(data)); console.log(step2(data)) });
