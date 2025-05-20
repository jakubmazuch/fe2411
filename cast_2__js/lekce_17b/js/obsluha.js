function vypisPromenne() {
    console.table({
        "a": a,
        "b": b,
        "honza": honza,
        "jirka": jirka,
    });
}

let a = 78;
let b = 28;
let honza = new Uzivatel("Jan Červený", 32);
let jirka = new Uzivatel("Jiří Veselý", 40);
vypisPromenne();

// Přiřazení
a = b;
honza = jirka;
vypisPromenne();

jirka.jmeno = "Martin Liška";
honza = new Uzivatel("Jan Modrý", 32);
vypisPromenne();