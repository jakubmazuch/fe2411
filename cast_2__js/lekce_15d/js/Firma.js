'use strict';

class Firma {

    constructor(nazev, sidlo) {
        this.nazev = nazev;
        this.sidlo = sidlo;
        this.zamestnanci = [];
    }
    vypisInfoOFirme() {
        document.write(`Firma ${this.nazev} sídlí v ${this.sidlo}.<br>`);
    }
    pridejZamestnance() {
        const jmeno = prompt("Zadejte jméno zaměstnance:");
        const prijmeni = prompt("Zadejte příjmení zaměstnance:");
        const vek = prompt("Zadejte věk zaměstnance:");
        const pozice = prompt("Zadejte pozici zaměstnance:");
        const zamestnanec = new Zamestnanec(jmeno, prijmeni, pozice, vek);
        this.zamestnanci.push(zamestnanec); // přídám zaměstanace do pole
    }
    vypisZamestnance() {
        document.write(`Zaměstnanci firmy ${this.nazev}:<br>`);
        const seznam = document.createElement("ul");
        for (const zamestnanec of this.zamestnanci) {
            seznam.innerHTML += `<li><strong>Jméno a příjmení: </strong>${zamestnanec.jmeno} ${zamestnanec.prijmeni}</li>`;
            seznam.innerHTML += `<li><strong>Pozice: </strong>${zamestnanec.pozice}</li>`;
            seznam.innerHTML += `<li><strong>Věk: </strong>${zamestnanec.vek}</li>`;
        }
        document.body.appendChild(seznam);
    }
}