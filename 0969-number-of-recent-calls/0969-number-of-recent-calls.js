
var RecentCounter = function() {
    this.arr = [null];
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.arr.push(t);
    let range = [t - 3000, t],
        counter = 0;
    for (let i = 1; i < this.arr.length; i++) {
        if (this.arr[i] >= range[0] && this.arr[i] <= range[1]) {
            counter++;
        }
    }
    return counter;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */