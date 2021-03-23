const my_boxes = [0, 1, 2, 3, 4, 5]

function logFirstBox(boxes) {
    console.log(boxes[0])
}

logFirstBox(my_boxes) // Will take 1 operation 
// no matter the size of the list
// Verdict: O(1)

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]);
    console.log(boxes[1]);
}

logFirstTwoBoxes(my_boxes) // Will take 2 operations always
// Verdict: O(2) -> O(1) - constant
