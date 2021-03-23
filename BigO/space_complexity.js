function boooo(array) {
    for (let i = 0; i < array.length; i++) {
        console.log("boooo!")
    }
}

boooo([1, 2, 3, 4, 5]) // O(1) space complexity


function arrayOfHiNTimes(array) {
    let hiArray = [];
    for (let i = 0; i < array.length; i++) {
        hiArray[i] = "hi";
    }
    return hiArray;
}

var returned_value = arrayOfHiNTimes([1, 2, 3, 4, 5])
console.log(returned_value)  // O(n) space complexity
