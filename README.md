# h2plusintegrator
H2+ Molecule Overlap Integral, Coulomb Integral and Exchange Integral Solver

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_A)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_A}{a_0}})

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_B)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_B}{a_0}})

![equation](https://latex.codecogs.com/gif.latex?S_{AB}(r)&space;=&space;\int&space;\Psi_{1,0,0}(r_A)&space;\Psi_{1,0,0}(r_B)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?\int&space;d^3&space;r&space;=&space;\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{\infty}&space;r^2&space;sin\theta&space;dr&space;d\theta&space;d\phi)

![equation](https://latex.codecogs.com/gif.latex?K(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_A)\frac{1}{r_B}&space;\Psi_{1,0,0}(r_B)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?J(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_A)\frac{1}{r_B}&space;\Psi_{1,0,0}(r_A)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?V(r)&space;=&space;\frac{e^2}{4\pi\epsilon_0}\frac{1}{r})

![equation](https://latex.codecogs.com/gif.latex?<E>_\pm&space;=&space;\frac{J\pm&space;K}{1&space;\pm&space;S_{AB}}&space;&plus;&space;\frac{e^2}{4\pi\epsilon_0}&space;\frac{1}{r})

![equation](https://latex.codecogs.com/gif.latex?<E>_\pm)

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_A))

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_B))

![equation](https://latex.codecogs.com/gif.latex?r_b=\sqrt{r_A^2&plus;R^2-2r_ARcos(\theta)})

is it possible ![equation](https://latex.codecogs.com/gif.latex?r_A=r) to use equation in line?
