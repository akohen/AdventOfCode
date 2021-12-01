fs = require('fs');

let tmp_max = 0

function process(lines) {
  const registers = {}

  for(let l of lines) {
    const line = l.split(" ")
    // test
    if( evaluate(line, registers)) {
      register(line[0],registers,line[1],line[2])
    }
  }

  let max = 0
  for(let r in registers) {
    if(registers[r] > max) {
      max = registers[r]
    }
  }
  return [tmp_max,max]
}

function register(r,registers,action="get",value=0) {
  if(registers[r] == null) {
    registers[r] = 0
  }

  if(action === 'inc') {
    registers[r] += Number(value)
  } else if(action === 'dec') {
    registers[r] -= Number(value)
  }
  tmp_max = Math.max(tmp_max,registers[r])

  return registers[r]
}

function evaluate(line, registers) {
  switch(line[5]) {
    case ">":
      return register(line[4],registers) > Number(line[6])
    case "<":
      return register(line[4],registers) < Number(line[6])
    case ">=":
      return register(line[4],registers) >= Number(line[6])
    case "<=":
      return register(line[4],registers) <= Number(line[6])
    case "==":
      return register(line[4],registers) == Number(line[6])
    case "!=":
      return register(line[4],registers) != Number(line[6])
  }

  return false
}

fs.readFile('input/day8','utf-8', (err, input) => {
  console.log( process(input.split("\n")) )
})
