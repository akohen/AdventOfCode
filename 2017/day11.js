fs = require('fs');

function day11(input) {
    let q = 0, r = 0, distance = 0;

    function dist() {
        return Math.max(Math.abs(q),Math.abs(r));
    }

    for(direction of input.split(',')) {
        if(direction === 's') {
            q--;
        } else if(direction === 'n') {
            q++
        } else if(direction === 'nw') {
            q++;
            r--;
        } else if(direction === 'ne') {
            r++;
        } else if(direction === 'sw') {
            r--;
        } else {
            q--;
            r++;
        }
        distance = Math.max(distance, dist())
    }

    return [dist(),distance]
}


fs.readFile('input/day11','utf-8', (err, data) => { console.log(day11(data)) });