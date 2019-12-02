fs = require('fs');

function day12(input) {
    const pattern = /(\d+) <-> (.+)/;
    const nodes = [];

    function createNode(id) { if(!nodes[id]) nodes[id] = {id: id, to: new Set()}; }

    // Build graph
    for(line of input.split("\n")) {
        const matches = line.match(pattern);
        const id = Number(matches[1])
        createNode(id);

        for(to of matches[2].split(", ")) {
            const destId = Number(to)
            createNode(destId);
            nodes[id].to.add(nodes[destId])
        }
    }

    // Traverse graph
    const search = [];
    let count = 0;
    for(node of nodes) {
        if(!node.seen) { 
            search.push(node);
            count++
        }

        while(search.length > 0) {
            const current = search.pop()
            current.seen = true;
            for(child of current.to) {
                if(!child.seen) {
                    search.push(child)
                }
            }
        }
    }

    return count
}


fs.readFile('input/day12','utf-8', (err, data) => { console.log(day12(data)) });