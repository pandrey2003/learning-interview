var my_array = [1, 2, 3, 4, 5, 6, 7, 8]


function functionWhichHasComplexName(items) {
    // This function prints the first item
    // then all items up to the middle of the list
    // then says 'hi' 100 times
    console.log(items[0]);
    var middle_index = Math.floor(items.length / 2)
    var index = 0

    while (index < middle_index) {
        console.log(items[index]);
        index++
    }
    for (let i = 0; i < 100; i++) { // O(100), not O(n)
        console.log('hi')
    }
}

functionWhichHasComplexName(my_array)
