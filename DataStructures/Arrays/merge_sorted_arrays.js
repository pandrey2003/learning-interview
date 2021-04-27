function mergeSortedArrays(arr1, arr2) {
    // Time complexity: O(n)
    // Space complexity: O(1)
    mergedArray = [];
    while (arr1 || arr2) {
        if (arr1.length === 0) {
            mergedArray.push(...arr2);
            break;
        }
        if (arr2.length === 0) {
            mergedArray.push(...arr1);
            break;
        }
        if (arr1[0] <= arr2[0]) {
            mergedArray.push(arr1[0]);
            arr1.splice(0, 1);
            continue;
        }
        mergedArray.push(arr2[0]);
        arr2.splice(0, 1);
    }
    return mergedArray;
}


if (require.main === module) {
    // Casual cases
    console.log(mergeSortedArrays([0,3,4,31], [4, 6, 30]));
    console.log(mergeSortedArrays([1, 2, 3, 4, 5], [2, 9, 11, 90]))
    // Extreme cases
    console.log(mergeSortedArrays([0,1], []))
    console.log(mergeSortedArrays([], []))
}
