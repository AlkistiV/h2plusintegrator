# h2plusintegrator
H₂⁺ Molecule Overlap Integral, Coulomb Integral and Exchange Integral Solver. 

The easiest possible molecule system is H₂⁺ ion consisting 2 protons and 1 electron. It can be investigated with Linear Combination of Atomic Orbitals (LCAO) method where the wave functions for the cases that the electron is bound to the nucleus A ![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_A)) or to the nucleus B ![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_B)) are linearly combined. They are defined as:

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_A)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_A}{a_0}}), ![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_B)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_B}{a_0}})

where ![equation](https://latex.codecogs.com/gif.latex?r_B) and ![equation](https://latex.codecogs.com/gif.latex?r_A) are relative distances of electron to respective proton;

![equation](https://latex.codecogs.com/gif.latex?r_B=\sqrt{r_A^2&plus;R^2-2r_ARcos(\theta)})

![equation](https://latex.codecogs.com/gif.latex?r_A=r)

![Sketch of 2 hydrogen nuclei and an electron](https://github.com/haltugyildirim/h2plusintegrator/blob/main/h_ions_sketch.svg "MSketch of 2 hydrogen nuclei and an electron")

Schematic of the ![equation](https://latex.codecogs.com/gif.latex?H_2^&plus;) ion[[2]](#2).

Normalization of the systems wavefunction creates an overlap integral. Overlap Integral S is defined as:

![equation](https://latex.codecogs.com/gif.latex?S_{AB}(r)&space;=&space;\int&space;\Psi_{1,0,0}(r_A)&space;\Psi_{1,0,0}(r_B)&space;d^3&space;r)

Where ![equation](https://latex.codecogs.com/gif.latex?d^3&space;r) is the triple integral in spherical coordinates;

![equation](https://latex.codecogs.com/gif.latex?\int&space;d^3&space;r&space;=&space;\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{\infty}&space;r^2&space;sin\theta&space;dr&space;d\theta&space;d\phi)

Even though the limit of r is infinite, values bigger than `100` generally breaks the code. But this upper limit seems to be producing consistent results.

Exchange or Resonance integral K is defined as;

![equation](https://latex.codecogs.com/gif.latex?K(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_A)\frac{1}{r_B}&space;\Psi_{1,0,0}(r_B)&space;d^3&space;r)

Coulomb integral J is defined as;

![equation](https://latex.codecogs.com/gif.latex?J(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_A)\frac{1}{r_B}&space;\Psi_{1,0,0}(r_A)&space;d^3&space;r)

V(r) is Coulomb potential;

![equation](https://latex.codecogs.com/gif.latex?V(r)&space;=&space;\frac{e^2}{4\pi\epsilon_0}\frac{1}{r})

Bonding and anti-bonding molecular orbitals 
![equation](https://latex.codecogs.com/gif.latex?<E>_\pm) are defined as;

![equation](https://latex.codecogs.com/gif.latex?<E>_\pm&space;=&space;\frac{J\pm&space;K}{1&space;\pm&space;S_{AB}}&space;&plus;&space;\frac{e^2}{4\pi\epsilon_0}&space;\frac{1}{r})

Integration is done with `scipy-integrate`. Resulting graph;

![integrals and cases graph](https://github.com/haltugyildirim/h2plusintegrator/blob/main/graph.svg "integrals and cases graph")


## Further
<a id="1">[1]</a> 
[The Case of H₂⁺ ](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Book%3A_Quantum_States_of_Atoms_and_Molecules_(Zielinksi_et_al)/10%3A_Theories_of_Electronic_Molecular_Structure/10.04%3A_The_Case_of_H%E2%82%82%E2%81%BA "The Case of H₂⁺ ")

<a id="2">[2]</a> 
[Das Wasserstoffmolekül-Ion](https://www.strands.de/chemical/39 "Das Wasserstoffmolekül-Ion")


<a id="3">[3]</a> 
[The Hydrogen Molecule Ion H2+ ](http://www.pci.tu-bs.de/aggericke/PC4e/Kap_II/H2-Ion.htm "The Hydrogen Molecule Ion H2+")
