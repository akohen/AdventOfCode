fs = require('fs');

function day3(input) {
    const claims = new Set()
    const duplicates = new Set()
    const pattern = /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/;

    for (line of input.split("\n")) {
        const [_, id, x, y, width, height] = line.match(pattern)
        for(let i=Number(x); i<Number(x)+Number(width); i++) {
            for(let j=Number(y); j<Number(y)+Number(height); j++) {
                const cell = `${i}/${j}`
                if(claims.has(cell)) {
                    duplicates.add(cell)
                } else {
                    claims.add(cell)
                }
            }
        }
    }

    checkline: for (line of input.split("\n")) {
        const [_, id, x, y, width, height] = line.match(pattern)
        for(let i=Number(x); i<Number(x)+Number(width); i++) {
            for(let j=Number(y); j<Number(y)+Number(height); j++) {
                const cell = `${i}/${j}`
                if(duplicates.has(cell)) { continue checkline; }
            }
        }
        return id
    }
        
    return duplicates.size

}


fs.readFile('input/day3','utf-8', (err, data) => { console.log(day3(data)) });