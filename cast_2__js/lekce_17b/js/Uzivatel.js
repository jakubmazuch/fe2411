class Uzivatel {
    constructor(jmeno, vek) {
        this.jmeno = jmeno;
        this.vek = vek;
    }
    toString() {
        return `${this.jmeno} (${this.vek})`;
    }
}