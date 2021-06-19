'use strict';

const log = (base, n) => Math.log(n) / Math.log(base)  // raising the level of abstraction
const createLog = base => n => log(base, n)

// Application
const lg = createLog(10)
const ln = createLog(Math.E)

console.log("lg(5) =", lg(5))
console.log("ln(9) =", ln(9))
