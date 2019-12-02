fs = require('fs');

function day4(input) {
    const log = input.split("\n").sort();
    const pattern = /\[\d+-\d+-(\d+) (\d+):(\d+)\][#A-Za-z ]+(\d+)?/;
    const guards = {};
    let current

    for(line of log) {
        const matches = line.match(pattern);

        if(matches[4]) {
            const id = Number(matches[4]);
            const time = (matches[2] == '23') ? 0 : Number(matches[3]);
            if(current) {guards[current.id] = current;}
            if(guards[id]) {
                current = guards[id];
                current.asleep = false;
                current.time = time;
            } else {
                current = { id:Number(matches[4]), sleep:[], asleep: false, time: time }
            }
        } else {
            current.asleep = !current.asleep;
            const newTime = Number(matches[3]);
            if(!current.asleep) {
                for(let i = current.time; i<newTime; i++) {
                    current.sleep.push(i)
                }
            }
            current.time = newTime;
        }
    }

    let guardId = 0, maxMinute = -1, max = 0;

    for(id in guards) {
        const guard = guards[id].sleep
        const counts = {};
        for(var i = 0; i < guard.length; ++i) {
            if(!counts[guard[i]]) counts[guard[i]] = 1;
            else ++counts[guard[i]];
        }

        for( minute in counts) {
            if(counts[minute] > max) {
                max = counts[minute]
                maxMinute = minute
                guardId = id
            }
        }

    }

    return [guardId * maxMinute]
}

fs.readFile('input/day4','utf-8', (err, data) => { console.log(day4(data)) });