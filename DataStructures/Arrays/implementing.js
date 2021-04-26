class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
       let lastItem = this.data[this.length-1];
       delete this.data[this.length-1];
       this.length--;
       return lastItem;
    }

    delete(index) {
        let deleteItem = this.data[index]
        delete this.data[index];
        this.length--;
        return deleteItem;
    }
}


const newArray = new MyArray();
newArray.push("abc");
newArray.push(1);
newArray.push(true);
console.log(newArray.pop());
console.log(newArray.delete(1));
console.log(newArray);
console.log(newArray.length);
