fs = require('fs');

function day1(input) {
    let result = 0
    const seen = new Set([0])


    while(true) {
        for (line of input.split("\n")) {
            result += Number(line)
            if(seen.has(result)) { 
                return result 
            } else {
                seen.add(result)
            }
        }
    }

}


fs.readFile('input/day1','utf-8', (err, data) => { console.log(day1(data)) });