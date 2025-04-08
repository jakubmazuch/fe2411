document.addEventListener("DOMContentLoaded", function () {
    let headerElements = document.querySelector("header");
    console.log(headerElements.childNodes);

    let nadpis = document.createElement("h2");
    nadpis.textContent = "Již třetí sezóna - legenda pokračuje!";
    let odstavec = document.getElementsByTagName("p");
    let main = document.querySelector("main");
    main.insertBefore(nadpis, odstavec[0]);
});