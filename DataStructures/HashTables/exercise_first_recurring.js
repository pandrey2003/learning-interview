function firstRecurringItem(arr) {
    // Checking for input
    console.log(typeof arr);
    if (typeof arr !== "object") {
        throw TypeError("Wrong input!");
    }
    // The code itself
    const hashTable = {};
    for (let element of arr) {
        if (hashTable[element]) {
            return element;
        }
        hashTable[element] = true;
    }
    return undefined;
}


// Testing - casual cases
console.log(firstRecurringItem([2,5,1,2,3,5,1,2,4]));
console.log(firstRecurringItem([2,1,1,2,3,5,1,2,4]));
console.log(firstRecurringItem([2,3,4,5]));
// Testing - extreme cases
console.log(firstRecurringItem([]));
//console.log(firstRecurringItem({}));
console.log(firstRecurringItem(12));
