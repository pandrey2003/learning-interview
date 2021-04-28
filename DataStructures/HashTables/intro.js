let user = {
    age: 54,
    name: "Kylie",
    magic: true,
    scream: function() {
        console.log("ahhhh!")
    },
}

user.age;  // O(1) for lookup, but not always
// on hash collisions it is O(n)
user.spell = "abrakadabra"  // O(1) for inserting

console.log(user);
