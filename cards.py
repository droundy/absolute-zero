from __future__ import division, print_function

import numpy, re, os, functools, random, string

os.system('mkdir -p cards')
fac = open('cards/.fac','w')

def negative(location):
    return r'''\node (names) [shape=circle, fill=\mybg, minimum width=1.0in] at (%s) {};
    \node (names) [shape=rectangle, fill=\myfg, minimum width=.6in, minimum height=.2in] at (%s) {};
''' % (location, location)
def positive(location):
    return r'''\node (names) [shape=circle, fill=\mybg, minimum width=1in] at (%s) {};
    \node (names) [shape=rectangle, fill=\myfg, minimum width=.6in, minimum height=.2in] at (%s) {};
    \node (names) [shape=rectangle, fill=\myfg, minimum width=.2in, minimum height=.6in] at (%s) {};
''' % (location, location, location)
def zero(location):
    return ''
    return r'''\node (names) [shape=circle, fill=\mybg, minimum width=1in] at (%s) {};
    \node (names) [shape=circle, fill=\mycolor, minimum width=.8in] at (%s) {};
''' % (location, location)


for color in ['red', 'blue', 'green', 'white']:
    if color == 'white':
        bg = 'black'
        fg = 'white'
    else:
        bg = 'white'
        fg = 'black'
    for number in range(-3,4):
        fac.write('| pdflatex %s%d\n\n' % (color, number))
        fac.write('| convert -density 300 %s%d.pdf -quality 90 %s%d.png\nc errors.log\n\n' % (color, number, color, number))
        with open('cards/%s%d.tex' % (color, number), 'w') as f:
            f.write(string.Template(r'''
\documentclass[11pt]{article}

\usepackage[paperwidth=2.75in,paperheight=3.75in,width=2.25in,height=3.25in]{geometry}
\usepackage{color}
\usepackage{tikz}

\pagestyle{empty}
\thispagestyle{empty}

\newcommand\mybg{$bg}
\newcommand\myfg{$fg}
\newcommand\mycolor{$color}

\begin{document}
  \color{\myfg}
  \begin{tikzpicture}[remember picture,overlay]
    \node [shape=rectangle, fill=$color, minimum height=\paperheight, minimum width=\paperwidth, anchor=south west] at (current page.south west) {};
    \node [shape=circle, fill=\mybg, minimum width=.5in, anchor=north west] at ([xshift=.25in, yshift=-.25in]current page.north west) { \Huge $number };
    \node [shape=circle, fill=\mybg, minimum width=.5in, anchor=north east] at ([xshift=-.25in, yshift=-.25in]current page.north east) { \Huge $number };
    \node [shape=circle, fill=\mybg, minimum width=.5in, anchor=north east, rotate=180] at ([xshift=.25in, yshift=.25in]current page.south west) { \Huge $number };
    \node [shape=circle, fill=\mybg, minimum width=.5in, anchor=north west, rotate=180] at ([xshift=-.25in, yshift=.25in]current page.south east) { \Huge $number };
''').substitute(color=color, number=number, bg=bg, fg=fg))
            if number < 0:
                drawing = negative
            else:
                drawing = positive
            if number == 0:
                f.write(zero('current page.center'))
            elif abs(number) == 1:
                f.write(drawing('current page.center'))
            elif abs(number) == 2:
                f.write(drawing('[yshift=.75in] current page.center'))
                f.write(drawing('[yshift=-.75in] current page.center'))
            elif abs(number) == 3:
                f.write(drawing('[yshift=.55in] current page.center'))
                f.write(drawing('[xshift=+.525in, yshift=-.35in] current page.center'))
                f.write(drawing('[xshift=-.525in, yshift=-.35in] current page.center'))
            f.write(string.Template(r'''
  \end{tikzpicture}
\end{document}
''').substitute(color=color, number=number))
