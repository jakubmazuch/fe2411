'use strict';

class Zvire {
    constructor(druh, pocetTlap, jmeno, vek) {
        this.druh = druh;
        this.pocetTlap = pocetTlap;
        this.jmeno = jmeno;
        this.vek = vek;
    }
    predstavSe() {
        document.write(`Jsem ${this.druh} a mám ${this.pocetTlap} tlap. Jmenuji se ${this.jmeno} a je mi ${this.vek} let. Těší mě. :)<br>`);
    }
}