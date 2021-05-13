function bubbleSort(array) {
    // Time complexity: O(n^2)
    // Space complexity: O(1)
    for (let trav_index=array.length; trav_index > 0; trav_index--) {
        for (let i=0; i < trav_index-1; i++) {
            if (array[i] > array[i+1]) {
                [array[i], array[i+1]] = [array[i+1], array[i]];
            }
        }
    }
    return array;
}

if (require.main === module) {
    console.log("Sorting [1, 5, 3, 2, 9, 8, 6]:",
    bubbleSort([1, 5, 3, 2, 9, 8, 6]));
    console.log("Sorting [7, 2, 1, 9, 3, 2]:",
    bubbleSort([7, 2, 1, 9, 3, 2]));
}
