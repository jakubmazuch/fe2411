let hlasy = [0, 0, 0];

const obrazky = [
    document.getElementById('obrSlon'),
    document.getElementById('obrTygr'),
    document.getElementById('obrZirafa')
];

const texty = [
    document.getElementById('hlasySlon'),
    document.getElementById('hlasyTygr'),
    document.getElementById('hlasyZirafa')
];

obrazky.forEach((obrazek, index) => {
    obrazek.addEventListener('click', () => {
        hlasy[index]++;
        texty[index].textContent = `Počet hlasů: ${hlasy[index]}`;
    });
});