function insertionSort(array) {
    // Time complexity: O(n^2)
    // Space complexity: O(1)
    for (let i=1; i < array.length; i++) {
        if (array[i] <= array[0]) {
            array.unshift(array.splice(i, 1)[0]);
            continue;
        }
        for (let trav_index=0; trav_index < i; trav_index++) {
            if (array[trav_index] <= array[i] && 
                array[i] <= array[trav_index+1]) {
                let poppedElement = array.splice(i, 1)[0];
                array.splice(trav_index+1, 0, poppedElement);
            }
        }
    }
    return array;
}


if (require.main === module) {
    console.log("Sorting [1, 5, 3, 2, 9, 8, 6]:",
    insertionSort([1, 5, 3, 2, 9, 8, 6]));
    console.log("Sorting [7, 2, 1, 9, 3, 2]:",
    insertionSort([7, 2, 1, 9, 3, 2]));
    console.log("Sorting [9, 0, 2, 6, 1, 18, 13]",
    insertionSort([9, 0, 2, 6, 1, 18, 13]))
}
