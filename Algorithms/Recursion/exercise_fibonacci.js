function fibonacciRecursive(n) {
    // 0, 1, 1, 2, 3, 5,...
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return 1;
    }
    return fibonacciRecursive(n-1)+fibonacciRecursive(n-2);
}

function fibonacciIterative(n) {
    // 0, 1, 1, 2, 3, 5,...
    let arr = [0, 1];
    for (let i = 2; i <=n; i++) {
        arr.push(arr[i-1] + arr[i-2]);
    }
    return arr[n];
}

if (require.main === module) {
    console.log(fibonacciRecursive(8));
    console.log(fibonacciIterative(8));
}
