var strings = ["a", "b", "c", "d"];
// 4*4 = 16 bytes of storage

console.log("The element on index 2 is:", strings[2]);  // O(1) for lookup

// push - O(1)
strings.push("e");

// pop - O(1)
strings.pop();

// insert (unshift for JS, insert for Python) - O(n)
strings.unshift("z");

// delete (splice for JS, remove for Python) - O(n)
strings.splice(2, 2);

console.log("Strings currently look like:", strings);
