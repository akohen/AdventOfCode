fs = require('fs');

function day2(input) {
    let twos = 0
    let threes = 0
    const lines = input.split("\n")

    function lettersCount(word) {
        let [two, three] = [0,0]
        const counts = {};
        word.split("").forEach(function(x) { counts[x] = (counts[x] || 0)+1; });

        for(letter in counts) {
            if (counts[letter] == 2) two = 1;
            if (counts[letter] == 3) three = 1;
        }
        return [two,three]
    }

    for (word of lines) {
        const [two, three] = lettersCount(word)
        twos += two
        threes += three
    }


    for(let i=0; i<lines.length; i++) {
        for(let j=i+1; j<lines.length; j++) {
            let diff = 0
            let result = ''
            for(let n=0; n<lines[i].length; n++) {
                if(lines[i][n] != lines[j][n]) { diff++ } else { result += lines[j][n]}
            }
            if(diff === 1) return result
        }
    }

    return twos * threes

}


fs.readFile('input/day2','utf-8', (err, data) => { console.log(day2(data)) });