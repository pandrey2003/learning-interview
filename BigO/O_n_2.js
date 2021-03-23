 // Log all pairs of array
const boxes = ['a', 'b', 'c', 'd', 'e']

function logAllPairs(boxes) {
    for (f_element of boxes) {
        for (s_element of boxes) {
            console.log([f_element, s_element]);
        }
    }
}

logAllPairs(boxes)
