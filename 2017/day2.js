fs = require('fs');

function day2(input) {
    let sum = 0

    for(line of input) {
        let min = Number.MAX_SAFE_INTEGER
        let max = -1
        for(n of line) {
            min = Math.min(n,min)
            max = Math.max(n,max)
        }
        sum += max - min
    }
    return sum
}


function day2_part2(input) {
    let sum = 0
    for(line of input) {
        line.some( (value, index) => {
            for (let i = index + 1; i<line.length; i++) {

                if(value > line[i]) { v1 = value; v2 = line[i] } 
                else { v1 = line[i]; v2 = value }

                if( v1%v2 == 0 ){
                    sum += v1 / v2
                    return true
                }
            }
        })
    }
    return sum
}


fs.readFile('input/day2','utf-8', (err, data) => { 
    const lines = data.split("\n")
    let array = []
    for(l of lines) {
        const values = l.split(" ").filter(i => i)
        let line = []
        values.map(v => { line.push(Number(v)) })
        array.push(line)
    }
    
    console.log(day2(array))
    console.log(day2_part2(array))
})

