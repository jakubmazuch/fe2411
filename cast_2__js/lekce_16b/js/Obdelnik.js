'use strict';

class Obdelnik {
    constructor(sirka, vyska) {
        this.sirka = sirka;
        this.vyska = vyska;
    }
    obsah() {
        return this.sirka * this.vyska;
    }
}