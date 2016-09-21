from __future__ import division

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy, re, os, functools, random

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

@functools.total_ordering
class Card(object):
    name = ''
    subjects = []
    history = []
    rarity = 'rare'
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
        value = re.sub(r' \(.+\)', '', value)
        value = re.sub(r'[\\$"]+', '', value)
        value = re.sub(r'^[-\s]*', '', value)
        value = re.sub(r'[-\s]+', '-', value)
        return value
    def __lt__(self, other):
        # there should be no different cards with identical names
        return re.sub(r'[\\$"]+', '', self.name.lower()) < re.sub(r'[\\$"]+', '', other.name.lower())
    def __eq__(self, other):
        # there should be no different cards with identical names
        return self.name == other.name
    def __ne__(self, other):
        # there should be no different cards with identical names
        return self.name != other.name

cards = []
cardMap = {}

subject_for_question = {}

aliases = {
    '2x': r'$2\times$',
    '3x': r'$3\times$',
    'sketch': 'sketch (diagram)',
    'diagram': 'sketch (diagram)',
    'spin 1/2 atom': r'spin $\frac12$ atom',
    'spin 1/2': r'spin $\frac12$',
    'Schrodinger equation': r'Schr\"odinger equation',
    'Schroedinger equation': r'Schr\"odinger equation',
    'Lambda system': r'$\Lambda$ system',

    'wavefunction': r'wave function',

    'small': r'small (short) (low)',
    'short': r'small (short) (low)',
    'low': r'small (short) (low)',

    'large': r'large (long) (high)',
    'long': r'large (long) (high)',
    'high': r'large (long) (high)',

    'box': 'box (chamber)',
    'chamber': 'box (chamber)',
}

def exam(number, subject, topics):
    subject_for_question[number] = subject
    for t in topics:
        if t in aliases:
            t = aliases[t]
        if t in cardMap:
            card = cardMap[t]
            card.history.append(number)
            card.subjects += [subject]
        else:
            card = Card(t, [subject], [number])
            cards.append(card)
            cardMap[t] = card

# Here are the exams
exam(123.1, 'q', [
    'quantum', 'point particle', 'mass', 'potential', 'gravity',
    'wave function', 'ground state', 'variational priciple'])
exam(123.2, 'q', [
    'electron', 'positron', 'spin', 'Hamiltonian', 'magnetic field',
    'eigenstate', 'energy'])
exam(123.3, 'e', [
    'rigid', 'metal', 'wire', 'plane', 'gravity', 'magnetic field',
    'width', 'length', 'mass', 'resistance', 'acceleration', 'force',
    'time', 'short', '2x'])
exam(123.4, 'e', [
    'Maxwell equations', 'dielectric', 'insulator',
    'dielectric permittivity', 'magnetic pemeability', 'monochromatic',
    'radiation', 'electric field', 'phase velocity', 'conductivity',
    'current', 'density', 'charge', 'free', 'wave', 'dispersion relation',
    'amplitude', 'small', 'attenuation', 'phase'])
exam(123.5, 't', [
    'polymer', 'chain', 'length', 'short', 'long', 'force', 'number',
    'energy', 'conservation', 'internal', 'temperature', 'work',
    'canonical ensemble', 'partition function', 'Helmholtz free energy',
    'small', 'spring constant', 'infinite'])
exam(123.6, 't', [
    'ideal gas', 'monatomic', 'temperature', 'volume', 'pressure', 'number',
    'atom', 'partition', 'chamber', 'second law of thermodynamics',
    'energy', 'work', 'entropy', 'information', 'measurement'])
exam(123.7, 'c', [
    'swing', 'mass', 'rope', 'massless', 'arc', 'radius', 'hoop',
    'rolling without slipping', 'gravity', 'equation of motion',
    'angle', 'small', 'equilibrium', 'frequency', 'oscillation'])
exam(123.8, 'c', [
    'solid', 'sphere', 'mass', 'radius', 'stationary', 'velocity',
    'angular', 'momentum', 'slips', 'friction', 'coefficient of friction',
    'moment of inertia', 'rolling without slipping', 'energy', 'kinetic',
    'heat', 'time', 'distance'])
exam(124.1, 'q', [
    'frequency', 'mass', 'Schrodinger equation', 'time', 'wave function',
    'simple harmonic oscillator',
    'eigenstate', 'energy', 'excited', 'expectation value'])
exam(124.2, 'q', [
    'electric field', 'energy', 'fixed', 'moment of inertia', 'rotate',
    'axle', 'small', 'wave function',
    'axis', 'charge', 'dipole moment', 'disk', 'eigenstate', 'eigenvalue'])
exam(124.3, 'e', [
    '2x', 'average', 'conductivity', 'time', 'uniform', 'voltage', 'AC',
    'plate', 'Poynting vector', 'small', 'large', 'magnetic',
    'susceptiblity', 'electric field', 'frequency', 'dielectric',
    'metal', 'disk', 'energy', 'dissipation', 'current', 'density'])
exam(124.4, 'e', [
    '2x', 'charge', 'density', 'distance',
    'electric field', 'far', 'frequency', 'hollow', 'magnetic field',
    'potential', 'rotate', 'sphere', 'surface', 'uniform', ])
exam(124.5, 't', [
    'cycle', 'efficiency', 'energy', 'engine', 'entropy', 'heat',
    'real gas', 'temperature', 'work'])
exam(124.6, 't', [
    'Lambda system', 'distinguishable', 'eigenstate', 'energy',
    'entropy', 'high', 'low', 'noninteracting', 'number', 'temperature'])
exam(124.7, 'c', [
    'oscillation', 'pendulum', 'small', 'spring', 'block',
    'equilibrium', 'frequency', 'frictionless', 'mass', 'normal modes'])
exam(124.8, 'c', [
    'train', 'velocity',
    'frictionless', 'mass', 'number', 'person', 'relative', 'speed'])
exam(125.1, 'q', [
    'magnetic moment', 'measurement', 'speed', 'spin 1/2', 'atom', 'spin',
    '2x', 'distance', 'eigenstate', 'eigenvalue', 'energy', 'magnetic field'])
exam(125.2, 'q', [
    'hydrogen atom', 'large', 'magnetic field', 'magnetic moment',
    'orbital', 'quantum', 'number', 'small',
    'atom', 'angular', 'momentum', 'degeneracy', 'electron', 'energy'])
exam(125.3, 'e', [
    'frequency', 'index of refraction', 'light', 'magnetic field', 'plasma',
    'Poynting vector', 'reflection', 'time', 'transmission', 'vacuum',
    'wave vector',
    'amplitude', 'average', 'dispersion relation', 'electric field', 'flux'])
exam(125.4, 'e', [
    'ground', 'infinite', 'metal', 'parallel', 'plate', 'potential',
    'surface', 'thickness',
    '2x', 'area', 'charge', 'density', 'distance', 'electric field'])
exam(125.5, 't', [
    'permeable', 'pressure', 'slow', 'temperature', 'volume',
    'impermeable', 'internal', 'monatomic', 'move', 'number', 'partition',
    '2x', 'atom', 'box', 'energy', 'entropy', 'equilibrium', 'ideal gas'])
exam(125.6, 't', [
    'rigid', 'temperature',
    'low', 'moment of inertia', 'number', 'quantum', 'rigid rotor',
    'angular', 'momentum', 'eigenvalue', 'energy', 'high', 'internal'])
exam(125.7, 'c', [
    'point', 'ring', 'spring', 'time', 'velocity',
    'frequency', 'frictionless', 'mass', 'normal modes', 'oscillation',
    '3x', 'constrained', 'coupled', 'equation of motion', 'equilibrium'])
exam(125.8, 'c', [
    '2x', 'angle', 'cylinder', 'equation of motion', 'gravity',
    'moment of inertia', 'rolling without slipping', 'solid', 'surface'])
exam(122.1, 'e', ['semi-infinite', 'electric', 'potential', '2x', 'plate',
                  'flat', 'metal', 'boundary conditions', 'series solution',
                  'approximation'])
exam(122.2, 'c', ['spring', 'ball', 'point', 'mass', 'sphere', 'immovable',
                  'wall', 'characteristic', 'natural', 'frequency', '2x',
                  'normal modes', 'infinite', 'neighbor', '1D'])
exam(122.3, 't', ["Curie's law", 'equation of state', 'paramagnet',
                  'internal', 'energy', 'magnetization', 'magnetic field',
                  'Carnot', 'engine', 'temperature',
                  'First Law of Thermodynamics', 'adiabatic', 'process',
                  'isothermal', 'heat', 'work', 'system', 'efficiency',
                  'cycle'])
exam(122.4, 'q', ['electron', 'charge', 'mass', 'infinite', 'potential',
                  'well', 'ground', 'state', 'excited', 'expectation value',
                  'energy', r'$|1\rangle$', r'$|2\rangle$', 'time', 'position'])
exam(122.5, 'c', ['steam', 'rotating', 'shaft', '2x', 'hinge', 'mass', 'slide',
                  'coplanar', 'point', 'angular', 'velocity', 'gravity', 'angle',
                  'position'])
exam(122.6, 'q', ['potential', 'well', '3x', 'step', 'infinity', 'wavefunction',
                  'ground', 'state', 'eigenstate', 'energy', 'probability',
                  'reflection', 'transmission'])
exam(122.7, 'e', ['charge', 'constant', 'volume', 'density', 'infinite',
                  'long', 'cylinder', 'radius', 'rotate', 'axis',
                  'angular', 'velocity', 'perpendicular', 'azimuthal', 'angle',
                  'symmetry', 'zero', 'current', 'density',
                  'cylindrical coordinates', 'magnetic field', 'outside',
                  'inside', 'distance'])
exam(122.8, 't', ['quantum', 'system', '3x', 'energy', 'level', '2x',
                  'identical', 'particle', 'temperature', 'heat', 'resevoir',
                  'state', 'configuration', 'Fermi-Dirac statistics',
                  'fermion', 'spin 1/2', 'up', 'Bose-Einstein statistics',
                  'spin 0', 'boson', 'classical',
                  'Maxwell-Boltzmann statistics'])
exam(121.1,'e',['wire', 'loop', 'circle', 'radius', 'current',  'angle',
                'cone', 'magnetic field', 'solenoid', 'infinite', 'small',
                'distance', 'axial'])
exam(121.2,'c',['mass', 'bead', 'constrained', 'gravity', 'frictionless',
                'wire', 'rotate', 'angular', 'velocity', 'Hamiltonian',
                'generalized', 'momentum', 'sketch', 'phase', 'energy',
                'oscillation'])
exam(121.3,'t',['adsorption', 'equilibrium', 'gas', 'pressure', 'box', 'volume',
                'metal','surface', 'energy', 'work', 'infinity', 'ideal gas',
                '2D', 'atom', 'partition function', 'free energy', 'chemical',
                'potential', 'number'])
exam(121.4,'q',['hydrogen', '2s', '2p', 'state', 'energy', 'electric field',
                'uniform', 'spin', 'degeneracy'])
exam(121.5,'c',['pendulum', '2x', 'point', 'mass', 'string', 'massless',
                'angular', 'motion', 'Lagrangian', 'harmonic'])
exam(121.6,'q',['free', 'particle', 'mass', 'constrained', 'circle', 'time',
                'wavefunction', 'angular', 'momentum', 'measurement',
                'energy', 'torus','system'])
exam(121.7,'e',['wave equation', 'electric field', 'magnetic field',
                'homogeneous', 'dielectric', 'free', 'charge', 'current',
                'vector space', 'coordinate system', 'Cartesian coordinates',
                'vector', 'scalar', 'velocity', 'wave', 'length', 'high',
                'limit'])
exam(121.8,'t',['Einstein', 'heat', 'capacity', 'simple harmonic oscillator',
                'frequency', 'energy', 'level', 'crystal', 'atom',
                'partition function', 'oscillator', 'temperature', 'low',
                'high'])
exam(120.1,'e',['metal', 'conducting', 'insulator', 'dielectric', 'sphere',
                'mass', 'radius', 'charge', 'surface', 'density', ])
exam(120.2,'c',['bead', 'mass', 'gravity', 'frictionless', 'surface',
                'point', 'particle', 'equation of motion', 'perturbation',
                'oscillation', 'angular', 'velocity', 'circle', 'height'])
exam(120.3,'t',['particle', 'spin 1/2', 'lattice', 'neighbor', 'Hamiltonian',
                'Ising model', 'spin', 'partition function', 'temperature',
                'energy', 'limit', 'entropy', ])
exam(120.4,'q',['potential', 'energy', 'nonrelativistic', 'particle',
                'mass', 'well', 'bound', 'state', 'continuous', 'barrier',
                'reflection', 'transmission', 'probability','momentum',])
exam(120.5,'t',['reversible', 'refridgerator', 'solid', 'temperature', 'heat',
                'engine', 'resevoir', 'efficiency', 'work',
                'capacity', 'entropy', 'internal', 'energy',])
exam(120.6,'q',['2x', 'spin 1/2', 'particle', 'mass', 'infinite', 'square',
                'well', 'width', 'eigenstate', 'energy', 'eigenvalue',
                'singlet', 'triplet', 'interaction', 'strength', 'length',
                'first-order', 'correction', 'interpret'])
exam(120.7,'c',['2x', 'mass','spring','constant', 'fixed', 'frictionless',
                'position', 'frequency', 'small', 'amplitude', 'oscillation',
                'stable', 'real', 'characteristic', 'normal modes',
                'trajectory', 'equilibrium'])
exam(120.8,'e',['insulator', 'ring', 'mass', 'charge', 'frictionless',
                'uniform', 'time', 'stationary', 'magnetic field', 'torque',
                'angular', 'momentum', 'infinity'])
exam(119.1,'c',['mass', 'gravity', 'drag', 'velocity', 'time', 'position',
                'zero', 'terminal', 'speed', 'limit'])
exam(119.2,'q',['identical', 'particle', '2x', '1D',
                'simple harmonic oscillator', 'potential', 'spring',
                'Hamiltonian', 'position', 'momentum', 'spin 0', 'boson',
                'state', 'degeneracy', 'energy', 'spin 1/2', 'fermion',
                'eigenvalue', 'small', 'interaction', 'confined',
                'perturbation', 'first-order', 'correction'])
exam(119.3,'t',['solid', 'nuclei', 'noninteracting', 'energy', 'spin 1/2',
                'ground', 'state', 'excited', 'uniform', 'magnetic field',
                'internal', 'temperature', 'heat', 'capacity', 'spin 1',
                'degenerate', 'high'])
exam(119.4,'e',['parallel', 'plate', 'capacitor', 'charge', 'air', 'radius',
                'current', 'wire', 'density', 'displacement', 'electric field',
                'induced', 'magnetic field', 'distance'])
exam(119.5,'c',['strong', 'weak', 'bond', 'oscillation', 'rigid', 'spring',
                'wall', 'Lagrangian', 'longitudinal', 'normal modes',
                'equilibrium', 'frequency', 'eigenvalue', '3x', 'atom',
                'stationary'])
exam(119.6,'q',['1D', 'ground','state', 'box', 'length', 'quickly', 'time',
                'expectation value', 'energy', 'probability', 'eigenstate',
                'wave function', 'zero'])
exam(119.7,'t',['van der Waals', 'gas', 'equation of state', 'abruptly',
                'free', 'expansion', 'heat', 'capacity', 'volume',
                'temperature'])
exam(119.8,'e',['plane', 'wave', 'angular', 'frequency', 'normally', 'incident',
                'metal', 'slab', 'power', 'reflection', 'conductivity',
                'interface'])
exam(118.1,'c',['infinite', 'number', 'mass', 'coupled', 'equilibrium',
                'string', 'tension', 'frictionless', 'transverse', 'small',
                'displacement', 'constrained', 'equation of motion', 'neighbor',
                'diagram', 'normal modes', 'wave', 'vector',
                'disperion relation', 'frequency', 'energy', 'infinity'])
exam(118.2,'q',['state', 'system', 'density matrix', 'spin 1/2', 'time',
                'trace'])
exam(118.3,'t',['noninteracting', 'atom', 'number', 'temperature',
                'magnetic field', 'volume', 'energy', 'angular', 'momentum',
                'moment', 'magnetization', 'low', 'temperature',
                'susceptiblity', 'high', 'sketch'])
exam(118.4,'e',['4x', 'point', 'charge', 'positive', 'square', 'distance',
                'force', 'motion', 'describe', 'equidistant'])
exam(118.5,'c',['pendulum', 'massless', 'disk', 'rotate', 'angular', 'velocity',
                'axis', 'Lagrangian', 'equation of motion', 'small',
                'frequency', 'simple harmonic oscillator'])
exam(118.6,'q',['electron', 'mass', 'symmetric', 'potential', 'angular',
                'momentum', 'hydrogen', 'atom', 'energy', 'eigenvalue',
                'ground', 'state', 'interaction', ])
exam(118.7,'t',['monatomic','gas', 'Carnot cycle', 'temperature',
                'isothermal', 'volume', 'heat', 'capacity', 'work',
                'entropy'])
exam(118.8,'e',['standing', 'wave', 'parallel', 'plates', 'metal', 'distance',
                'vacuum', 'electric field', 'magnetic field', 'time', 'surface',
                'charge', 'density', 'position'])

num_cards = 107

total_history = sum([len(c.history) for c in cards])
history_per_copy = total_history/num_cards
print 'history_per_copy', history_per_copy
cards.sort() # first sort alphabetically
cards.sort(key=lambda x: len(x.history))
cumulative_history = 0
cumulative_rarity = 'rare'
for c in cards:
    cumulative_history += len(c.history)
    if cumulative_history > 2*total_history/3:
        cumulative_rarity = 'ubiquitous'
    elif cumulative_history > total_history/3:
        cumulative_rarity = 'common'
        ubiquitous_limit = len(c.history)
    else:
        common_limit = len(c.history)
    c.rarity = cumulative_rarity
ubiquitous = sorted([c for c in cards
                     if c.rarity == 'ubiquitous'])
rares = sorted([c for c in cards
                if c.rarity == 'rare'])
commons = sorted([c for c in cards
                  if c.rarity == 'common'])
cards.reverse()
copies_left = -1
while copies_left < 0:
    copies_left = num_cards
    for c in cards:
        ncopy = int(round(len(c.history)/history_per_copy))
        c.copies = ncopy
        copies_left -= ncopy
    history_per_copy *= 1.01 # try a bit fewer

for c in cards:
    if copies_left > 0:
        c.copies += 1
        copies_left -= 1
    else:
        break

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
    f.write(r'''\end{enumerate}

    \clearpage
    \section{Ubiquitous cards (%d)}
\begin{enumerate}
''' % len(ubiquitous))
    for card in ubiquitous:
        f.write(r'\item %s (%d)  $\times %d$' % (card.name,
                                                 len(card.history),
                                                 card.copies) + '\n')
    f.write(r'''\end{enumerate}

    \section{Common cards (%d)}
\begin{enumerate}
''' % len(commons))
    for card in commons:
        f.write(r'\item %s (%d)  $\times %d$' % (card.name,
                                                 len(card.history),
                                                 card.copies) + '\n')
    f.write(r'''\end{enumerate}

    \section{Rare cards (%d)}
\begin{enumerate}
''' % len(rares))
    for card in rares:
        f.write(r'\item %s (%d)  $\times %d$' % (card.name,
                                                 len(card.history),
                                                 card.copies) + '\n')
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
    'c': numpy.array([0,1,0]), # '#00ff00',
    'q': numpy.array([1,1,0]), # '#ffff00',
    't': numpy.array([1, 9/16, 0]), # '#ff9900',
    'e': numpy.array([2/16, 5/16, 1]), # '#2255ff',
}

# The following is an almost-undocumented feature that makes usetex
# text have a correct baseline alignment.
plt.rcParams['text.latex.preview'] = True
plt.rcParams['axes.linewidth'] = 2*lining*72
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{graphicx}'
]
# os.system('rm -rf cards-rare cards-ubiquitous cards-common cards-count')
for d in ['cards-rare', 'cards-ubiquitous', 'cards-common', 'cards-count']:
    try:
        os.mkdir(d)
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
    hist = {}
    for x in card.subjects:
        # randomize a bit so we won't get equal results for two
        # subjects
        hist[x] = hist.get(x,0) + random.gauss(1, 0.001)
    card.subjects.sort(key=lambda x: hist[x])
    meancolor = numpy.zeros(3)
    for i in range(len(card.subjects)):
        ymin = i*(cardy-2*lining)/len(card.subjects)/2+lining
        ymax = (i+1)*(cardy-2*lining)/len(card.subjects)/2+lining
        plt.axhspan(ymin, ymax, color=bgcolors[card.subjects[i]])
        ymin = cardy - i*(cardy-2*lining)/len(card.subjects)/2-lining
        ymax = cardy - (i+1)*(cardy-2*lining)/len(card.subjects)/2-lining
        plt.axhspan(ymin, ymax, color=bgcolors[card.subjects[i]])
        meancolor += bgcolors[card.subjects[i]]
    meancolor /= meancolor.max()
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, cardx)
    plt.ylim(0, cardy)
    bigtext = r'\resizebox{!}{!}{} ' + '\n'.join(card.name.split(' '))
    # print 'bigtext:', bigtext
    bigtext = re.sub(r'\n\((.+)\)', '\n'+r'\\textit{\1}', bigtext)
    # print '        ', bigtext
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
    edge_name = r'\normalsize{%s}' % (card.name)
    edge_name = re.sub(r' \(.+\)', '', edge_name)
    plt.text(edge_offset, cardy-2*border,
             edge_name,
             rotation=90,
             color='white',
             rotation_mode='anchor',
             horizontalalignment='right',
             verticalalignment='baseline',)
    plt.text(cardx-edge_offset, 2*border,
             edge_name,
             rotation=270,
             color='white',
             rotation_mode='anchor',
             horizontalalignment='right',
             verticalalignment='baseline',)
    percent_frequency = len(card.history)/len(subject_for_question)*100
    rarity_text = r'\tiny{\em %s (%.0f\%%)}' % (card.rarity, percent_frequency)
    if percent_frequency <= 0.5:
        rarity_text = r'\tiny{\em %s}' % (card.rarity)
    rarity_offset = 1.0*border
    plt.text(cardx/2, rarity_offset,
             rarity_text,
             rotation=0,
             color=meancolor,
             rotation_mode='anchor',
             horizontalalignment='center',
             verticalalignment='baseline',)
    plt.text(cardx/2, cardy-rarity_offset,
             rarity_text,
             rotation=180,
             color=meancolor,
             rotation_mode='anchor',
             horizontalalignment='center',
             verticalalignment='baseline',)
    # plt.savefig('cards-{}/{}.png'.format(card.rarity,
    #                                      card.filename()),
    #             dpi=300)
    if card.copies > 0:
        plt.savefig('cards-count/{}[{}].png'.format(card.filename(),
                                                    card.copies),
                    dpi=300)
    plt.close()
