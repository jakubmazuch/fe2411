document.addEventListener("DOMContentLoaded", function () {
    let elements = document.getElementsByClassName("important");
    let odstavec = document.getElementsByTagName("p");  
    for (let i = 0; i < elements.length; i++) {
        console.log(elements[i]);
    }
    for (let i = 0; i < odstavec.length; i++) {
        console.log(odstavec[i]);
    }

    let zmena = document.querySelector("span");
    zmena.textContent = "provozní době koupaliště";

    let doba = document.querySelectorAll("li");
    let ctvrtek = doba[3];
    console.log(ctvrtek.innerHTML);

    let logoObrazek = document.querySelector("#logo");
    console.log(logoObrazek.hasAttribute("alt"));

    // zvýraznění dnešního dne
    const dnes = new Date().getDay(); // 0 = neděle, 1 = pondělí, ..., 6 = sobota
    const mapovani = [6,0,1,2,3,4,5]; // mapování pro správné pořadí
    const seznamDnu = document.querySelectorAll("ul li");

    const dnesniDen = seznamDnu[mapovani[dnes]];
    dnesniDen.classList.add("important");
});