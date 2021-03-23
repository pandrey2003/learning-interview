// Importing the performance module
const {performance} = require('perf_hooks');

// The actual code
const nemo = ['nemo'];
const everyone = [
    'dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat',
  
    'nigel', 'squirt', 'darla', 'hank'
]
const large = new Array(10000).fill('nemo')

function findNemo(array) {
    let t0 = performance.now();
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
    let t1 = performance.now();
    console.log('Call to Nemo took ' + (t1-t0) + ' milliseconds.')
}

findNemo(large);
// Time is often not a factor... Big O helps to distinguish between
// a good code and a bad code.
