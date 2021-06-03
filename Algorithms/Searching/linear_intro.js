var beasts = ["Centaur", "Godzilla", "Mosura", "Minotaur", "Hydra"];

// All the methods for beasts below are linear
console.log(beasts.indexOf('Godzilla'));

console.log(beasts.findIndex(function(item){
    return item === "Godzilla";
}));

console.log(beasts.find(function(item){
    return item === "Godzilla";
}));

console.log(beasts.includes("Godzilla"));
