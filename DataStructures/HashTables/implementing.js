class HashTable {
    constructor(size){
      this.data = new Array(size);
    }
  
    _hash(key) {
      let hash = 0;
      for (let i =0; i < key.length; i++){
          hash = (hash + key.charCodeAt(i) * i) % this.data.length
      }
      return hash;
    }

    set(key, value) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data;
    }

    get(key) {
        let address = this._hash(key);
        let currentBucket = this.data[address];
        if (currentBucket && currentBucket.length >= 1) {
            for (let subBucket of currentBucket) {
                if (subBucket[0] === key) {
                    return subBucket[1];
                }
            }
        }
        return undefined;
    }

    keys() {
        const keysArray = [];
        for (let element of this.data) {
            if (element) {
                keysArray.push(element[0][0])
            }
        }  // this would become O(n^2)
        // if taking into account hash collisions
        return keysArray;
    }
}


const myHashTable = new HashTable(50);
console.log(myHashTable.set("grapes", 100));
console.log(myHashTable.set("apples", 54));
console.log(myHashTable.set("oranges", 10))
console.log(myHashTable.get("grapes"));
console.log(myHashTable.get("banana"));
console.log("");
console.log(myHashTable.keys());
