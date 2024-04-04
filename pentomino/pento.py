'''Definiert die Pento Class und ein paar interne Funktionen für
die Initialisierung.
Die einzelnen Steine sind flach und werden mit vier Offset-Koordinatenpaaren
relativ zu einem Würfel auf dem Koordinatenpunkt (0,0) beschrieben.
Beispiel P-Stück:
    XX      (0,0), (0,1)
    XX      (1,0), (1,1)
    X       (2,0)
Die Reihenfolge der Paare ist egal. Im Konstruktor von Pento wird dann
eine Liste der möglichen Positionen in 3D relativ zu jedem der Würfel im
Stein generiert:
Für jeden Würfelpunkt je vier Rotationen um die x-, y- und z-Achse.
Anschließend wird diese Liste normalisiert und doppelte Einträge werden
entfernt.

'''
import numpy as np
KOORD_REL = {
    'P': [(0,0), (1,0), (0,1), (1,1), (2,0)],
    'I': [(0,0), (1,0), (2,0), (3,0), (4,0)],
    'L': [(0,0), (1,0), (2,0), (3,0), (3,1)],
    'F': [(0,0), (0,1), (1,1), (2,1), (1,2)],
    'X': [(0,0), (-1,0), (1,0), (0,-1), (0,1)],
    'U': [(0,0), (0,2), (1,0), (1,1), (1,2)],
    'W': [(0,0), (1,0), (1,1), (2,1), (2,2)],
    'Y': [(0,0), (1,0), (2,0), (3,0), (1,1)],
    'Z': [(0,0), (0,1), (1,1), (2,1), (2,2)],
    'N': [(0,0), (1,0), (2,0), (2,1), (3,1)],
    'T': [(0,0), (0,1), (0,2), (1,1), (2,1)],
    'V': [(0,0), (1,0), (2,0), (2,1), (2,2)]
}

#
# Das sind die Rotationsgruppe in 3D für Drehungen um 90°
# Die Rotationsmatrizen wegen leichterer Lesebarkeit kodiert mit +, -, .
# für +1, -1 und 0.
#
_ROTATIONS = [
 '+...+...+', '+....-.+.', '+...-...-', '+....+.-.', '.-.+....+', '..++...+.',
 '.+.+....-', '..-+...-.', '-...-...+', '-....-.-.', '-...+...-', '-....+.+.',
 '.+.-....+', '..+-...-.', '.-.-....-', '..--...+.', '..-.+.+..', '.+...++..',
 '..+.-.+..', '.-...-+..', '..-.-.-..', '.-...+-..', '..+.+.-..', '.+...--..'
]
_CHAR2NUM = {
	'.': 0,
	'+': +1,
	'-': -1
}
ROTATIONS = [
    np.array([_CHAR2NUM[char] for char in rotation]).reshape((3,3))
    for rotation in _ROTATIONS]

_pentominos = {}
def get_pentominos():
    '''return _pentominos
    '''
    if len(_pentominos) == 0:
        for typ, koord  in KOORD_REL.items():
            _pentominos[typ] = Pento(typ, koord)
    return _pentominos

class Pento():
    ''' Pentominoes mit Beschreibung ihrer Lagen
    '''
    def __init__(self, typ, koord):
        self.typ = typ
        self.koord2d = koord
        koord3d = np.zeros((5,3), dtype=np.int8)
        koord3d[:, :2] = np.array(self.koord2d)
        self.positions = np.array(generate_all_pos(koord3d))

    def __repr__(self):
        return f'Pento-{self.typ:s}, positions: {len(self.positions)}'
    def show(self):
        '''Darstellung Stein als ASCII-Kunst
        '''
        raum = np.zeros((7,7), dtype=np.int8)
        punkt = (1,1)
        punkte = np.array(self.koord2d) + punkt
        for coord_xy in punkte:
            coord_x, coord_y = coord_xy
            raum[coord_x, coord_y] = ord(self.typ)
        print(':')
        # pylint: disable=unbalanced-tuple-unpacking
        # pylint: disable=no-member
        coord_x, coord_y = raum.nonzero()
        inhalt = raum[
                coord_x.min(): coord_x.max()+1,
                coord_y.min(): coord_y.max()+1]
        for zeile in inhalt:
            text = ' '.join(chr(o) if o > 0 else '.' for o in zeile)
            print(f"\t{text}")

def generate_all_pos(koord3d):
    '''Ausgehend von der Startverteilung:
       - Schiebe jeden Würfel auf (0,0,0)
       - Rotiere jede der 5 Verteilungen
       Eliminiere doppelte Verteilungen
    '''

    def hash_pos(matrix):
        '''Wir bilden aus der Matrix einen Hash-String, weil wir
           - für das Dictionary einen inmutable Key brauchen
           - die Koordinaten der 5 Positionen sortieren wollen 
        '''
        return ''.join(str(x) for x in (matrix+5).flatten())

    all_pos = []
    for element in set_00(koord3d):
        for rotation in ROTATIONS:
            all_pos.append(np.array(sorted(element @ rotation, key=hash_pos)))

    return list(
        {hash_pos(element): element for element in all_pos}.values()
    )

def set_00(koord3d):
    ''' doc missing
    '''
    return [np.array(koord3d) - origin for origin in koord3d]
