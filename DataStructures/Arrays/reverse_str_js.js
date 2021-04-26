function reverseString(string) {
    // check input
    if (!string || string.length < 2 || typeof string !== "string") {
        throw TypeError;
    }
    return string.split("").reverse().join("");
}

let reverseAdvanced = string => [...string].reverse().join("");


console.log(reverseString("abc"));
console.log(reverseAdvanced("Andrew"));
// console.log(reverseString(undefined));
