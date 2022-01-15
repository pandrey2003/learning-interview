function containsCommonItem(arr1, arr2) {
    // loop through first array and create obj
    // where properties === items in the array
    let map = {};
    for (let i=0; i < arr1.length; i++) {
        if (!map[i]) {
            const item = arr1[i];
            map[item] = true;
        }
    }
    // loop through second array and check if item
    // in second array exists on created obj
    for (let j=0; j < arr2.length; j++) {
        if (map[arr2[j]]) {
            return true
        }
    }
    return false
}

containsCommonItem(["a", "b"], [])
// O(a+b)

function containsCommonItem3(arr1, arr2) {
    // The language-specific solution
    return arr1.some(item => arr2.includes(item))
}

console.log(containsCommonItem3(["a", "b"], ["a"]))
