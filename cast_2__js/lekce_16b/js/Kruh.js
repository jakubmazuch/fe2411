'use strict';

class Kruh {
    constructor(prumer) {
        this.prumer = prumer;
    }
    obsah() {
        return Math.PI * (this.prumer/2) * (this.prumer/2);
    }
}