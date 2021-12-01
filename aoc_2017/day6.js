fs = require('fs');

function day6(memory) {
    const seen = new Set()
    const memory2 = memory.slice()

    while(!seen.has(JSON.stringify(memory))) {
        seen.add(JSON.stringify(memory))
        reallocateMemory(memory)
    }

    const target = JSON.stringify(memory)
    let beforeCycle = 0
    while(JSON.stringify(memory2) != target) {
        reallocateMemory(memory2)
        beforeCycle++
    }

    return [seen.size,seen.size - beforeCycle]
}

function reallocateMemory(memory) {
    const len = memory.length

    // selecting next bank to spread 
    let maxIndex = len - 1
    for (let i = len - 2; i >= 0; i--) {
        if( memory[i] >= memory[maxIndex] ) {
            maxIndex = i
        }
    }

    // spread
    const spread = memory[maxIndex]
    memory[maxIndex] = 0
    for (let i = maxIndex + 1; i<=maxIndex+spread;i++) {
        memory[i%len]++
    }
}


fs.readFile('input/day6','utf-8', (err, input) => { 
    const data = []
    input.split(" ").filter(i => i).map(v => data.push(Number(v)))
    
    console.log(data)
    console.log(day6(data))
})

