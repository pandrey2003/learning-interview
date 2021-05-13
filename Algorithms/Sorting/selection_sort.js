function selectionSort(array) {
    // Time complexity: O(n^2)
    // Space complexity: O(1)
    for (let trav_index=array.length; trav_index > 0; trav_index--) {
        for (let i=array.length-trav_index+1; i < array.length; i++) {
            if (array[i] < array[array.length-trav_index]) {
                [array[i], array[array.length-trav_index]] = 
                [array[array.length-trav_index], array[i]];
            }
        }
    }
    return array;
}

if (require.main === module) {
    console.log("Sorting [1, 5, 3, 2, 9, 8, 6]:",
    selectionSort([1, 5, 3, 2, 9, 8, 6]));
    console.log("Sorting [7, 2, 1, 9, 3, 2]:",
    selectionSort([7, 2, 1, 9, 3, 2]));
}
