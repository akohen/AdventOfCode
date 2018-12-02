fs = require('fs');

function Disc(name, weight, parent = null) {
    this.weight = weight
    this.name = name
    this.parent = parent
    this.children = []
    this.sum = weight    
}


fs.readFile('input/day7','utf-8', (err, input) => { 
    const lines = input.split("\n")
    const elements = {}
    let top = null

    // building the tree
    for (var i = lines.length - 1; i >= 0; i--) {
        const matches = lines[i].match(/^(\w+) \((\d+)\)( -> (.*))?$/)
        let disc = elements[matches[1]]
        let weight = Number(matches[2])
        if( !disc ) {
            disc = new Disc(matches[1], weight)
            elements[matches[1]] = disc
        } else {
            disc.weight = weight
            disc.sum = weight
        }

        if( matches[3] ) {
            matches[4].split(", ").map(i => {
                let child = elements[i]
                if( child ) {
                    child.parent = disc
                } else {
                    child = new Disc(i,-1,disc)
                    elements[i] = child
                }
                disc.children.push(child)
            })
        }

        top = disc
    }

    // add the weights
    for(let key in elements) {
        let node = elements[key]
        let weight = node.weight
        while(node.parent) {
            node = node.parent
            node.sum += weight
        }
    }

    // finding the root
    while(top.parent) {
        top = top.parent
    }

    const nodesToCheck = [top]
    let current = null
    let offset = 0 // if != 0, this value has to be added to the imbalanced node

    while( nodesToCheck.length > 0) {
        current = nodesToCheck.pop()
        const seen = {}

        // count occurrences of each sum among the children
        for(let child of current.children ) {
            if( !(child.sum in seen) ) {
                seen[child.sum] = []
            }
            seen[child.sum].push(child)
        }


        // Add to list all sums occurring only once (can be 0-2)
        for(let value in seen) {
            if(seen[value].length == 1) {
                nodesToCheck.push(seen[value][0])

                if(current == top) { // get offset at top level
                    for(let other in seen) {
                        if (other != value) {
                            offset = other - value
                        }
                    }
                }

            }
        }


    }

    console.log(top.name)
    console.log(current.weight + offset)
})
