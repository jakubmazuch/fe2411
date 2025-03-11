let hlasySlon = 0;
let hlasyTygr = 0;
let hlasyZirafa = 0;

const obrSlon = document.getElementById('obrSlon');
const obrTygr = document.getElementById('obrTygr');
const obrZirafa = document.getElementById('obrZirafa');

const textSlon = document.getElementById('hlasySlon');
const textTygr = document.getElementById('hlasyTygr');
const textZirafa = document.getElementById('hlasyZirafa');

obrSlon.addEventListener('click', function () {
    hlasySlon++;
    textSlon.textContent = `Počet hlasů: ${hlasySlon}`;
});
obrTygr.addEventListener('click', function () {
    hlasyTygr++;
    textTygr.textContent = `Počet hlasů: ${hlasyTygr}`;
});
obrZirafa.addEventListener('click', function () {
    hlasyZirafa++;
    textZirafa.textContent = `Počet hlasů: ${hlasyZirafa}`;
});