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
    'spin 1/2 atom': r'spin $\frac12$ atom',
    'Schrodinger equation': r'Schr\"odinger equation',
    'Schroedinger equation': r'Schr\"odinger equation',
    'Lambda system': r'$\Lambda$ system',
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
    'magnetic moment', 'measurement', 'speed', 'spin 1/2 atom', 'spin',
    '2x', 'distance', 'eigenstate', 'eigenvalue', 'energy', 'magnetic field'])
exam(125.2, 'q', [
    'hydrogen atom', 'large', 'magnetic field', 'magnetic moment',
    'orbital', 'quantum', 'number', 'small',
    'atom', 'angular momentum', 'degeneracy', 'electron', 'energy'])
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
    'angular momentum', 'eigenvalue', 'energy', 'high', 'internal'])
exam(125.7, 'c', [
    'point', 'ring', 'spring', 'time', 'velocity',
    'frequency', 'frictionless', 'mass', 'normal modes', 'oscillation',
    '3x', 'constrained', 'coupled', 'equation of motion', 'equilibrium'])
exam(125.8, 'c', [
    '2x', 'angle', 'cylinder', 'equation of motion', 'gravity',
    'moment of inertia', 'rolling without slipping', 'solid', 'surface'])

total_history = sum([len(c.history) for c in cards])
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
os.system('rm -rf cards-rare cards-ubiquitous cards-common')
for d in ['cards-rare', 'cards-ubiquitous', 'cards-common']:
    os.mkdir(d)
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
    #bigtext = r'\resizebox{!}{!}{} '+card.name
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
             r'\normalsize{%s}' % (card.name),
             rotation=90,
             color='white',
             rotation_mode='anchor',
             horizontalalignment='right',
             verticalalignment='baseline',)
    plt.text(cardx-edge_offset, 2*border,
             r'\normalsize{%s}' % (card.name),
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
    plt.savefig('cards-{}/{}.png'.format(card.rarity,
                                         card.filename()),
                dpi=300)
    plt.close()
