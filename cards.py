from __future__ import division

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy, re, os

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class Card(object):
    name = ''
    subjects = []
    history = []
    def __init__(self, n, s=[], history=[]):
        self.subjects = s
        self.name = n
        self.history = history
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
        value = re.sub(r'[\\$"]+', '', value)
        value = re.sub(r'^[-\s]*', '', value)
        value = re.sub(r'[-\s]+', '-', value)
        return value

cards = []

def newcard(name, history=[]):
    if len(history) > 0:
        cards.append(Card(name,
                          list({subject_for_question[i] for i in history}),
                          history))

subject_for_question = {
    124.1: 'q',
    124.2: 'q',
    124.3: 'e',
    124.4: 'e',
    124.5: 't',
    124.6: 't',
    124.7: 'c',
    124.8: 'c',
    125.1: 'q',
    125.2: 'q',
    125.3: 'e',
    125.4: 'e',
    125.5: 't',
    125.6: 't',
    125.7: 'c',
    125.8: 'c',
}

newcard(r'$2\times$', [124.3, 124.4, 125.1, 125.4, 125.5, 125.8])
newcard(r'$3\times$', [125.7])
newcard(r'$\infty\times$')
newcard(r'2-level system')
newcard(r'3-level system', [124.5])
newcard(r'Hamiltonian')
newcard(r'atom', [125.2, 125.5])
newcard(r'air')
newcard(r'amplitude', [125.3])
newcard(r'angle', [125.8])
newcard(r'angular momentum', [125.2, 125.6])
newcard(r'area', [125.4])
newcard(r'axis', [124.2])
newcard(r'axle', [124.1])
newcard(r'average', [124.3, 125.3])
newcard(r'bar')
newcard(r'box', [125.5])
newcard(r'charge', [124.2, 124.4, 125.4])
newcard(r'collision')
newcard(r'conductivity', [124.3])
newcard(r'confined')
newcard(r'conserved')
newcard(r'constrained', [125.7])
newcard(r'coupled', [125.7])
newcard(r'current', [124.3])
newcard(r'cycle', [124.5])
newcard(r'cylinder', [125.8])
newcard(r'degeneracy', [125.2])
newcard(r'density', [124.3, 124.4, 125.4])
newcard(r'dielectric', [124.3])
newcard(r'dipole moment', [124.2])
newcard(r'disk', [124.2, 124.3])
newcard(r'dispersion relation', [125.3])
newcard(r'dissipation', [124.3])
newcard(r'distance', [124.4, 125.1, 125.4])
newcard(r'distinguishable', [124.6])
newcard(r'efficiency', [124.5])
newcard(r'eigenstate', [124.1, 124.2, 124.6, 125.1])
newcard(r'eigenvalue', [124.2, 125.1, 125.6])
newcard(r'eigenvectors')
newcard(r'electric field', [124.2, 124.3, 124.4, 125.3, 125.4])
newcard(r'electron', [125.2])
newcard(r'energy', [124.1, 124.2, 124.3, 124.5, 124.6,
                    125.1, 125.2, 125.5, 125.6])
newcard(r'engine', [124.5])
newcard(r'entropy', [125.5, 124.5, 124.6])
newcard(r'equation of motion', [125.7, 125.8])
newcard(r'equilibrium', [125.5, 125.7, 124.7])
newcard(r'excited', [124.1])
newcard(r'even')
newcard(r'expectation value', [124.1])
newcard(r'far', [124.4])
newcard(r'fast')
newcard(r'finite')
newcard(r'fixed', [124.2])
newcard(r'flux', [125.3])
newcard(r'force')
newcard(r'frequency', [124.1, 124.3, 124.4, 124.7, 125.3, 125.7])
newcard(r'friction')
newcard(r'frictionless', [125.7, 124.7, 124.8])
newcard(r'fulcrum')
newcard(r'glass')
newcard(r'gravity', [125.8])
newcard(r'ground', [125.4])
newcard(r'harmonic')
newcard(r'heat', [124.5])
newcard(r'high', [125.6, 124.6])
newcard(r'hinge')
newcard(r'hollow', [124.4])
newcard(r'hydrogen atom', [125.2])
newcard(r'ideal gas', [125.5])
newcard(r'impermeable', [125.5])
newcard(r'inclined')
newcard(r'infinite', [125.4])
newcard(r'index of refraction', [125.3])
newcard(r'internal', [125.5, 125.6])
newcard(r'kinetic energy')
newcard(r'large', [125.2, 124.3])
newcard(r'light', [125.3])
newcard(r'low', [125.6, 124.6])
newcard(r'magnetic', [124.3])
newcard(r'magnetic field', [125.1, 125.2, 125.3, 124.4])
newcard(r'magnetic moment', [125.1, 125.2])
newcard(r'mass', [124.1, 125.7, 124.7, 124.8])
newcard(r'measurement', [125.1])
newcard(r'metal', [124.3, 125.4])
newcard(r'moment of inertia', [124.2, 125.6, 125.8])
newcard(r'momentum')
newcard(r'monatomic', [125.5])
newcard(r'move', [125.5])
newcard(r'noninteracting', [124.6])
newcard(r'normal modes', [125.7, 124.7])
newcard(r'nucleus')
newcard(r'number', [125.2, 125.5, 125.6, 124.6, 124.8])
newcard(r'odd')
newcard(r'orbital', [125.2])
newcard(r'oscillation', [125.7, 124.7])
newcard(r'parallel', [125.4])
newcard(r'partition', [125.5])
newcard(r'pendulum', [124.7])
newcard(r'period')
newcard(r'permeable', [125.5])
newcard(r'person', [124.8])
newcard(r'pivot')
newcard(r'plane wave')
newcard(r'plane')
newcard(r'plasma', [125.3])
newcard(r'plate', [124.3, 125.4])
newcard(r'point', [125.7])
newcard(r'position')
newcard(r'potential', [125.4, 124.4])
newcard(r'Poynting vector', [124.3, 125.3])
newcard(r'pressure', [125.5])
newcard(r'probability')
newcard(r'pulley')
newcard(r'quantum', [125.6, 125.2])
newcard(r'radiation')
newcard(r'real gas', [124.5])
newcard(r'relative', [124.8])
newcard(r'reflection', [125.3])
newcard(r'remove')
newcard(r'rigid rotor', [125.6])
newcard(r'rigid', [125.6])
newcard(r'ring', [125.7])
newcard(r'rolling without slipping', [125.8])
newcard(r'rope')
newcard(r'rotate', [124.2, 124.4])
newcard(r'Schr\"odinger equation', [124.1])
newcard(r'simple harmonic oscillator', [124.1])
newcard(r'sliding')
newcard(r'slow', [125.5])
newcard(r'small', [124.2, 124.3, 124.7, 125.2])
newcard(r'solid', [125.8])
newcard(r'speed', [125.1, 124.8])
newcard(r'sphere', [124.4])
newcard(r'spherical')
newcard(r'spin $\frac12$ atom', [125.1])
newcard(r'spin 1 atom')
newcard(r'spin', [125.1, 125.2])
newcard(r'spring', [125.7, 124.7])
newcard(r'square well')
newcard(r'static')
newcard(r'string')
newcard(r'surface', [125.4, 125.8, 124.4])
newcard(r'susceptiblity', [124.3])
newcard(r'symmetry')
newcard(r'temperature', [125.5, 125.6, 124.5, 124.6])
newcard(r'tension')
newcard(r'thickness', [125.4])
newcard(r'time', [124.1, 124.3, 125.3, 125.7])
newcard(r'train', [124.8])
newcard(r'transmission', [125.3])
newcard(r'uncertainty')
newcard(r'uniform', [124.3, 124.4])
newcard(r'vacuum', [125.3])
newcard(r'volume', [125.5])
newcard(r'water')
newcard(r'wave function', [124.1, 124.2])
newcard(r'wave vector', [125.3])
newcard(r'work', [124.5])
newcard(r'velocity', [125.7, 124.8])
newcard(r'voltage', [124.3])

with open('cards.tex', 'w') as f:
    f.write(r'''\documentclass[twocolumn]{article}

\usepackage{graphicx}

\begin{document}

\section{Classical}
\begin{enumerate}
''')
    for card in cards:
        num = len([h for h in card.history if subject_for_question[h] == 'c'])
        if num > 0:
            f.write(r'\item %s (%d)' % (card.name, num) + '\n')
    f.write(r'''\end{enumerate}

    \section{Quantum}
\begin{enumerate}
''')
    for card in cards:
        num = len([h for h in card.history if subject_for_question[h] == 'q'])
        if num > 0:
            f.write(r'\item %s (%d)' % (card.name, num) + '\n')
    f.write(r'''\end{enumerate}

    \section{Thermal}
\begin{enumerate}
''')
    for card in cards:
        num = len([h for h in card.history if subject_for_question[h] == 't'])
        if num > 0:
            f.write(r'\item %s (%d)' % (card.name, num) + '\n')
    f.write(r'''\end{enumerate}

    \section{E\&M}
\begin{enumerate}
''')
    for card in cards:
        num = len([h for h in card.history if subject_for_question[h] == 'e'])
        if num > 0:
            f.write(r'\item %s (%d)' % (card.name, num) + '\n')
    ubiquitous_limit = 5
    common_limit = 1
    ubiquitous = [c for c in cards
                  if len(c.history) > ubiquitous_limit]
    commons = [c for c in cards
               if len(c.history) > common_limit and len(c.history) <= ubiquitous_limit]
    rares = [c for c in cards
             if len(c.history) > 0 and len(c.history) <= common_limit]
    f.write(r'''\end{enumerate}

    \section{Ubiquitous cards (%d)}
\begin{enumerate}
''' % len(ubiquitous))
    for card in ubiquitous:
        f.write(r'\item %s (%d)' % (card.name, len(card.history)) + '\n')
    f.write(r'''\end{enumerate}

    \section{Common cards (%d)}
\begin{enumerate}
''' % len(commons))
    for card in commons:
        f.write(r'\item %s (%d)' % (card.name, len(card.history)) + '\n')
    f.write(r'''\end{enumerate}

    \section{Rare cards (%d)}
\begin{enumerate}
''' % len(rares))
    for card in rares:
        f.write(r'\item %s (%d)' % (card.name, len(card.history)) + '\n')
    f.write(r'''\end{enumerate}

\end{document}
''')

cardx = 2.25
cardy = 3.5
border = 0.125 # the extra bit that is cut off
lining = 2.5*border # the thickness of the black edge on the card
bordercolor = '#000000'
bgcolor = '#eeeeee'
bgcolors = {
    'c': '#00ff00',
    'q': '#ffff00',
    't': '#ff9900',
    'e': '#2255ff',
}

# The following is an almost-undocumented feature that makes usetex
# text have a correct baseline alignment.
plt.rcParams['text.latex.preview'] = True
plt.rcParams['axes.linewidth'] = 2*lining*72
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{graphicx}'
]
try:
    os.mkdir('card-output')
except:
    pass
for card in cards:
    fig = plt.figure(figsize=(cardx + 2*border, cardy + 2*border))
    plt.subplots_adjust(left=border/(cardx+2*border),
                        right=(border+cardx)/(cardx+2*border),
                        top=(border+cardy)/(cardy+2*border),
                        bottom=border/(cardy+2*border))
    for s in plt.axes().spines.values():
        s.set_color(bordercolor)
    for i in range(len(card.subjects)):
        ymin = i*(cardy-2*lining)/len(card.subjects)+lining
        ymax = (i+1)*(cardy-2*lining)/len(card.subjects)+lining
        plt.axhspan(ymin, ymax, color=bgcolors[card.subjects[i]])
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, cardx)
    plt.ylim(0, cardy)
    bigtext = r'\resizebox{!}{!}{} ' + '\n'.join(card.name.split(' '))
    #bigtext = r'\resizebox{!}{!}{} '+card.name
    print '%s' % bigtext
    txt = plt.text(cardx/2, cardy*.5, bigtext,
                   size=16,
                   horizontalalignment='center',
                   verticalalignment='top',)

    renderer1 = fig.canvas.get_renderer()
    bbox1 = txt.get_window_extent(renderer1)
    txt.remove()

    fontsize = 1.5*72/bbox1.width*16
    altfontsize = 1*72/bbox1.height*16
    fontsize = min(fontsize, altfontsize)
    plt.text(cardx/2, cardy*.3, bigtext,
             size = fontsize,
             rotation=180,
             horizontalalignment='center',
             verticalalignment='center',)

    plt.text(cardx/2, cardy*.7, bigtext,
             size = fontsize,
             horizontalalignment='center',
             verticalalignment='center',)

    edge_offset = 2.0*border
    plt.text(edge_offset, cardy-2*border,
             r'\normalsize{%s (%d)}' % (card.name, len(card.history)),
             rotation=90,
             color='white',
             rotation_mode='anchor',
             horizontalalignment='right',
             verticalalignment='baseline',)
    plt.text(cardx-edge_offset, 2*border,
             r'\normalsize{%s (%d)}' % (card.name, len(card.history)),
             rotation=270,
             color='white',
             rotation_mode='anchor',
             horizontalalignment='right',
             verticalalignment='baseline',)
    plt.savefig('card-output/'+card.filename()+'.png', dpi=300)
    print 'did', card.filename()
    plt.close()
