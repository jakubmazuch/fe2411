'use strict';

window.addEventListener('DOMContentLoaded', () => {
    const tlacitko = document.getElementById('button');
    const vystup = document.getElementById('vystup');

    tlacitko.addEventListener('click', () => {
        const lev = new Zvire('lev', 4, 'Alex', 5);
        const zebra = new Zvire('zebra', 4, 'Marty', 3);
        const zirafa = new Zvire('žirafa', 4, 'Melman', 6);
        const hroch = new Zvire('hroch', 4, 'Gloria', 3);
        const tucnak = new Zvire('tučnák', 2, 'Kowalski', 1);
        
        vystup.innerHTML = `
        <p>${lev.predstavSe()}</p>
        <p>${zebra.predstavSe()}</p>
        <p>${zirafa.predstavSe()}</p>
        <p>${hroch.predstavSe()}</p>
        <p>${tucnak.predstavSe()}</p>
        `; 
    })
});
