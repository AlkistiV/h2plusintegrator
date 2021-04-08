# h2plusintegrator
H2+ Molecule Overlap Integral, Coulomb Integral and Exchange Integral Solver

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_a)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_a}{a_0}})

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_b)&space;=&space;\sqrt{\frac{1}{\pi}}{a_0}^{-\frac{3}{2}}{e}^{-\frac{r_b}{a_0}})

![equation](https://latex.codecogs.com/gif.latex?S_{ab}(r)&space;=&space;\int&space;\Psi_{1,0,0}(r_a)&space;\Psi_{1,0,0}(r_b)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?\int&space;d^3&space;r&space;=&space;\int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{\i}&space;r^2&space;sin\theta&space;dr&space;d\theta&space;d\phi)

![equation](https://latex.codecogs.com/gif.latex?K(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_a)\frac{1}{r_b}&space;\Psi_{1,0,0}(r_b)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?J(r)&space;=&space;-\frac{e^2}{4\pi\epsilon_0}&space;\int&space;\Psi_{1,0,0}(r_a)\frac{1}{r_b}&space;\Psi_{1,0,0}(r_a)&space;d^3&space;r)

![equation](https://latex.codecogs.com/gif.latex?V(r)&space;=&space;\frac{e^2}{4\pi\epsilon_0}\frac{1}{r})

![equation](https://latex.codecogs.com/gif.latex?<E>_\pm&space;=&space;\frac{J\pm&space;K}{1&space;\pm&space;S_{ab}}&space;&plus;&space;\frac{e^2}{4\pi\epsilon_0}&space;\frac{1}{r})

![equation](https://latex.codecogs.com/gif.latex?<E>_\pm)

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_a))

![equation](https://latex.codecogs.com/gif.latex?\Psi_{1,0,0}&space;(r_b))

![equation](https://latex.codecogs.com/gif.latex?r_b=\sqrt{r_a^2&plus;R^2-2r_aRcos(\theta)})

is it possible ![equation](https://latex.codecogs.com/gif.latex?r_a=r) to use equation in line?
