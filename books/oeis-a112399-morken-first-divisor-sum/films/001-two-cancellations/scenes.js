'use strict';

const heading = (label, title) => {
  txt(label, 150, 174, { size: 30, fam: F.mono, c: C.cyan, ls: 5 });
  txt(title, 150, 259, { size: 55, fam: F.orb, c: C.white });
};

const card = (x, y, width, label, value, alpha, colour) => {
  panel(x, y, width, 152, alpha, colour, label);
  txt(value, x + width / 2, y + 102, { size: 46, fam: F.mono, align: 'center', c: colour, a: alpha });
};

SCENES.sieve = S => {
  heading('A112399   /   THE SIEVE', 'Which scores survive?');
  const scores = {1: '+1', 3: '−1', 7: '−1', 9: '0'};
  for (let index = 1; index <= 10; index++) {
    const kept = Object.hasOwn(scores, index);
    const alpha = kept ? 1 : 1 - 0.72 * at(S, 0, 0.8, index * 0.13);
    card(150 + (index - 1) * 162, 380, 144, String(index), kept ? scores[index] : '×', alpha, kept ? C.cyan : C.white);
  }
  txt('C₁₀(10) = +1 − 1 − 1 + 0 = −1', W / 2, 700, { size: 55, fam: F.mono, c: C.now, align: 'center', a: at(S, 1, 0.8) });
};

SCENES.pair = S => {
  heading('ROUTE 1   /   DIVISORS', 'Match opposite signs');
  card(150, 365, 770, 'INDEX 6 · SHARED PRIME 2', 'μ(1) + μ(2) = 0', 1, C.cyan);
  card(980, 365, 770, 'INDEX 7 · NO SHARED PRIME', 'μ(1) = 1', at(S, 1, 0.7), C.now);
  txt('The weights multiply the original Möbius score.', W / 2, 645, { size: 35, c: C.white, align: 'center', a: at(S, 1, 0.8) });
};

SCENES.powers = S => {
  heading('ROUTE 2   /   ALLOWED PRIMES', 'Split the copies of two');
  const divisors = [1, 2, 4, 8];
  const scores = ['0', '0', '−1', '+1'];
  divisors.forEach((divisor, index) => {
    const alpha = at(S, 1, 0.65, index * 0.33);
    card(150 + index * 402, 386, 370, `q = ${divisor}  ·  8/q = ${8 / divisor}`, scores[index], alpha, index < 2 ? C.white : C.now);
  });
  txt('All prime factors of 4 and 8 divide 10.', W / 2, 648, { size: 37, c: C.cyan, align: 'center' });
};

SCENES.cutoff = S => {
  heading('TWO IDENTITIES   /   ONE FILTER', 'The cutoff can move');
  card(150, 360, 765, 'PRIMES TO EXCLUDE', 'n = 10', 1, C.cyan);
  const cutoff = [6, 10, 14][Math.min(2, Math.floor(S.u / 2))];
  card(985, 360, 765, 'LAST INDEX TO COUNT', `X = ${cutoff}`, 1, C.now);
  txt('Jamie Morken · OEIS A112399', W / 2, 640, { size: 36, c: C.white, align: 'center', a: at(S, 1, 0.6) });
  txt('Haobo Ma and Wenlin Zhang · version 3', W / 2, 705, { size: 31, c: C.cyan, align: 'center', a: at(S, 1, 0.6) });
};

FILM.poster = () => {
  const scene = TL.scenes[0];
  const moment = scene.start + 3;
  background(moment, scene, 0, TL.scenes.length);
  grid(moment, 0.6);
  heading('A112399   /   VERSION 3', 'Two ways to cancel');
  txt(DATA.film.title_zh, 150, 348, { size: 52, fam: F.zh, c: C.white });
  card(150, 455, 765, 'THE SIEVE', '1, 3, 7, 9', 1, C.cyan);
  card(985, 455, 765, 'THE SCORE', '+1 − 1 − 1 + 0 = −1', 1, C.now);
  txt('Jamie Morken · Haobo Ma and Wenlin Zhang', 150, 795, { size: 32, c: C.white });
  post(3);
};
