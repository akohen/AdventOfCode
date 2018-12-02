fs = require('fs');

function day4(input) {
    let sum = 0
    for (passphrase of input) {
        if(isValid(passphrase)) {
            sum++
        }
    }
    return sum
}


function isValid(passphrase) {
    const seen = new Set()
    for(word of passphrase) {
        if (seen.has(word)) {
            return false
        } else {
            seen.add(word)
        }
    }
    return true
}



fs.readFile('input/day4','utf-8', (err, input) => { 
    const lines = input.split("\n")
    let data = []
    for(l of lines) {
        const values = l.split(" ").filter(i => i)
        let line = []
        values.map(v => { line.push(v.split('').sort().join('')) })
        data.push(line)
    }
    
    console.log(day4(data))
})

