fs = require('fs');
/*
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10  27 
21  22  23  24  25  26
*/
function day3(n) {
    // 1 is on ring 0
    //  9 (=3x3) is the 1st "ring leader" / ring 2 => 25 = 5x5 / ring 3 => 49 = 7x7
    // 11/15/19/23 make up the "cross" of the second ring

    // ring i contains numbers up to (2i+1)²

    // Step 1 : finding the ring (finding the first ring-leader bigger or equal to n)
    // Step 2 : find the distance to the "cross"
    // Step 3 : add distance to cross with ring number to get distance to 1

    // Ring
    let ring = 0
    while (n > (2*ring + 1)**2) {
        ring++
    }

    const ringLeader = (2*ring + 1)**2
    const cross = [
        ringLeader - ring,
        ringLeader - 3*ring,
        ringLeader - 5*ring,
        ringLeader - 7*ring,
    ]

    let distanceToCross = ring
    for(point of cross) {
        distanceToCross = Math.min(distanceToCross,Math.abs(point - n))
    }


    return ring + distanceToCross
}

console.log(day3(289326))


