# This file is part of Fisheater, A strong 4 player chess engine,
# and is released under the "GNU General Public License v3.0". Please see the LICENSE
# file that should have been included as part of this package.
#------------------------------------------------------------------------------------

coordinates = [
                         'd14', 'e14', 'f14', 'g14', 'h14', 'i14', 'j14', 'k14',
                         'd13', 'e13', 'f13', 'g13', 'h13', 'i13', 'j13', 'k13',
                         'd12', 'e12', 'f12', 'g12', 'h12', 'i12', 'j12', 'k12',
    'a11', 'b11', 'c11', 'd11', 'e11', 'f11', 'g11', 'h11', 'i11', 'j11', 'k11', 'l11', 'm11', 'n11',
    'a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10', 'j10', 'k10', 'l10', 'm10', 'n10',
    'a9',  'b9',  'c9',  'd9',  'e9',  'f9',  'g9',  'h9',  'i9',  'j9',  'k9',  'l9',  'm9',  'n9',
    'a8',  'b8',  'c8',  'd8',  'e8',  'f8',  'g8',  'h8',  'i8',  'j8',  'k8',  'l8',  'm8',  'n8',
    'a7',  'b7',  'c7',  'd7',  'e7',  'f7',  'g7',  'h7',  'i7',  'j7',  'k7',  'l7',  'm7',  'n7',
    'a6',  'b6',  'c6',  'd6',  'e6',  'f6',  'g6',  'h6',  'i6',  'j6',  'k6',  'l6',  'm6',  'n6',
    'a5',  'b5',  'c5',  'd5',  'e5',  'f5',  'g5',  'h5',  'i5',  'j5',  'k5',  'l5',  'm5',  'n5',
    'a4',  'b4',  'c4',  'd4',  'e4',  'f4',  'g4',  'h4',  'i4',  'j4',  'k4',  'l4',  'm4',  'n4',
                         'd3',  'e3',  'f3',  'g3',  'h3',  'i3',  'j3',  'k3',
                         'd2',  'e2',  'f2',  'g2',  'h2',  'i2',  'j2',  'k2',
                         'd1',  'e1',  'f1',  'g1',  'h1',  'i1',  'j1',  'k1',
]

def parseFenAndReturnGameState():
    """ Parse The Fen And Get The Game State
    