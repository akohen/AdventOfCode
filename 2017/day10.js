fs = require('fs');

function day10(input) {
    const circle = []
    let skip = 0;
    let current = 0;
    for(let i=0; i<256; i++) { circle.push(i); }
    const twists = []
    let result = ""

    for(letter of input) {
        twists.push(letter.charCodeAt(0))
    }
    twists.push(17, 31, 73, 47, 23)

    for(let counter=0; counter<64; counter++) {
        for(twist of twists) {
            const len = Number(twist)
            for(let i=current, j=current+len-1; i<j; i++, j--) {
                let tmp = circle[i%circle.length];
                circle[i%circle.length] = circle[j%circle.length];
                circle[j%circle.length] = tmp;
            }
            current = (current + len + skip)%circle.length
            skip++
        }
    }
    
    for(let i=0; i<16; i++) {
        let dense = 0
        for(let j=0; j<16; j++) {
            dense = dense ^ circle[i*16+j]
        }
        result += ("00" + dense.toString(16)).substr(-2)
    }

    return result
}


fs.readFile('input/day10','utf-8', (err, data) => { console.log(day10(data)) });