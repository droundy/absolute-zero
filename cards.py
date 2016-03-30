import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy, re, os
matplotlib.rc('text', usetex=True)

class Card(object):
    subjects = []
    name = ''
    def __init__(self, n, s=[]):
        self.subjects = s
        self.name = n
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def filename(self):
        """
        Normalizes string, converts to lowercase, removes non-alpha characters,
        and converts spaces to hyphens.
        """
        value = self.name
        value = re.sub(r'[\\$]+', '', value)
        value = re.sub(r'^[-\s]*', '', value)
        value = re.sub(r'[-\s]+', '-', value)
        return value

cards = []

def newcard(name, s=[]):
    cards.append(Card(name, s))

newcard(r'$2\times$', ['c', 'q'])
newcard(r'$3\times$', ['c', 'q'])
newcard(r'$\infty\times$', ['c', 'q'])
newcard(r'2-level system', ['q'])
newcard(r'3-level system', ['q'])
newcard(r'Hamiltonian', ['q'])
newcard(r'air', ['c'])
newcard(r'angle', ['c'])
newcard(r'angular momentum', ['q'])
newcard(r'axis', ['c', 'q'])
newcard(r'axle', ['c'])
newcard(r'bar', ['c'])
newcard(r'box', ['c'])
newcard(r'charge', ['c', 'q'])
newcard(r'collision', ['c'])
newcard(r'confined', ['c', 'q'])
newcard(r'conserved', ['c'])
newcard(r'constrained', ['c'])
newcard(r'cylinder', ['c'])
newcard(r'dipole moment', ['c'])
newcard(r'disk', ['c'])
newcard(r'eigenstate', ['q'])
newcard(r'eigenvalue', ['q'])
newcard(r'eigenvectors', ['c'])
newcard(r'electric field', ['c', 'q'])
newcard(r'electron', ['c', 'q'])
newcard(r'energy', ['c', 'q'])
newcard(r'equation of motion', ['c'])
newcard(r'equilibrium', ['c'])
newcard(r'even', ['q'])
newcard(r'expectation value', ['q'])
newcard(r'fast', ['q'])
newcard(r'finite', ['c', 'q'])
newcard(r'force', ['c'])
newcard(r'frequency', ['c'])
newcard(r'friction', ['c'])
newcard(r'frictionless', ['c'])
newcard(r'fulcrum', ['c'])
newcard(r'glass', ['c'])
newcard(r'gravity', ['c'])
newcard(r'harmonic', ['q'])
newcard(r'hinge', ['c'])
newcard(r'hollow', ['c'])
newcard(r'hydrogen atom', ['q'])
newcard(r'inclined', ['c'])
newcard(r'infinite', ['c', 'q'])
newcard(r'kinetic energy', ['c'])
newcard(r'large', ['c', 'q'])
newcard(r'light', ['q'])
newcard(r'magnetic field', ['c', 'q'])
newcard(r'magnetic moment', ['c', 'q'])
newcard(r'mass', ['c', 'q'])
newcard(r'measurement', ['q'])
newcard(r'moment of inertia', ['c', 'q'])
newcard(r'momentum', ['c', 'q'])
newcard(r'normal modes', ['c'])
newcard(r'nucleus', ['q'])
newcard(r'odd', ['q'])
newcard(r'oscillating', ['c'])
newcard(r'oscillation', ['q'])
newcard(r'partition', ['c'])
newcard(r'period', ['c'])
newcard(r'pivot', ['c'])
newcard(r'plane wave', ['q'])
newcard(r'plane', ['c'])
newcard(r'point particle', ['c', 'q'])
newcard(r'position', ['q'])
newcard(r'potential energy', ['c'])
newcard(r'probability', ['q'])
newcard(r'pulley', ['c'])
newcard(r'radiation', ['q'])
newcard(r'reflection', ['q'])
newcard(r'remove', ['q'])
newcard(r'rigid rotor', ['q'])
newcard(r'rigid', ['c'])
newcard(r'ring', ['c'])
newcard(r'roll without slipping', ['c'])
newcard(r'rope', ['c'])
newcard(r'simple harmonic oscillator', ['q'])
newcard(r'slab', ['c'])
newcard(r'sliding', ['c'])
newcard(r'slow', ['q'])
newcard(r'small', ['c', 'q'])
newcard(r'solid', ['c'])
newcard(r'sphere', ['c'])
newcard(r'spherical', ['q'])
newcard(r'spin $\frac12$ atom', ['q'])
newcard(r'spin 1 atom', ['q'])
newcard(r'spin', ['q'])
newcard(r'spring', ['c'])
newcard(r'square well', ['q'])
newcard(r'static', ['c', 'q'])
newcard(r'string', ['c'])
newcard(r'symmetry', ['q'])
newcard(r'tension', ['c'])
newcard(r'time', ['q'])
newcard(r'transmission', ['q'])
newcard(r'uncertainty', ['q'])
newcard(r'water', ['c'])
newcard(r'wave function', ['q'])

with open('cards.tex', 'w') as f:
    f.write(r'''\documentclass[twocolumn]{article}

\begin{document}
\section{Classical}
\begin{enumerate}
''')
    for card in cards:
        if 'c' in card.subjects:
            f.write(r'\item ' + str(card) + '\n')
    f.write(r'''\end{enumerate}

    \section{Quantum}
\begin{enumerate}
''')
    for card in cards:
        if 'q' in card.subjects:
            f.write(r'\item ' + str(card) + '\n')
    f.write(r'''\end{enumerate}

\end{document}
''')

cardx = 2.25
cardy = 3.5
border = 0.125

os.system('rm -rf card-output')
try:
    os.mkdir('card-output')
except:
    pass
for card in cards:
    plt.figure(figsize=(cardx + 2*border, cardy + 2*border))
    plt.subplots_adjust(left=border/(cardx+2*border))
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, cardx)
    plt.ylim(0, cardy)
    plt.title(card.name)
    plt.savefig('card-output/'+card.filename()+'.png', dpi=300)
    plt.close()
