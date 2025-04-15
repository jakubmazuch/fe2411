'use strict';

const smajlik = new Kruh(50);
const oko = new Kruh(11);
const usta = new Obdelnik(20,5);
const obsahZluteCasti = smajlik.obsah() - usta.obsah() - (2*oko.obsah());

document.write(`<p>Obsah žluté části je ${obsahZluteCasti} cm<sup>2</sup>.</p>`)