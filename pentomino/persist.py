''' Persistierung eines Problems (gelöst oder ungelöst)
Benutzt shelve. Die Datenbank heißt pentomino.db in dem Verzeichnis
laut $SELVEDIR.
Ist $SELVEDIR nicht gesetzt, landet es im package einen höher als
dieses Module.
'''
import os
from pathlib import Path
import shelve

from pentomino.problems import build

DB = os.environ.get('SHELVEDIR', Path(__file__).parents[1] ) / 'pentomino'
print(f'Shelve-File ist {DB}.db')

def save(raum, prefix=None):
    ''' - 
    '''
    prefix = gen_prefix(raum) if prefix is None else prefix

    with shelve.open(DB, flag='c') as db:
        try:
            cnt = max(
                version_as_int(key) for key in db.keys()
                if key.startswith(prefix)
            )
        except ValueError: # keys() is empty
            cnt = 0
        else:
            cnt += 1

        key= f'{prefix}_{cnt}'
        db[key] = raum

    return key

def version_as_int(key):
    ' xxxxx_yy_nnn -> int(nnn)'
    version = key.rsplit('_', maxsplit=1)[1]
    return int(version)

def get_versions(prefix):
    ' -> sorted( (k, v) ) '
    with shelve.open(DB, flag='r') as db:
        return sorted(
            (
                (key, val) for key, val in db.items() if key.startswith(prefix)
            )
        )

def get_keys(prefix=None):
    ''' -
    '''
    with shelve.open(DB, flag='r') as db:
        if prefix is None:
            return list(db.keys())

        return [key for key in db.keys() if key.startswith(prefix)]

def get_obj(key):
    ''' -
    '''
    with shelve.open(DB, flag='r') as db:
        return db.get(key)

def pop(key):
    ''' -
    '''
    with shelve.open(DB, flag='w') as db:
        obj =  db.get(key)
        if obj is not None:
            del db[key]
            print(f'remove_obj: {key}')
        return obj

def gen_prefix(raum):
    ''' -
    '''
    trimmed_wo_hull = build.trim_with_empty_hull(raum)[1:-1, 1:-1, 1:-1]
    shape = trimmed_wo_hull.shape

    return  str(shape).replace(', ', '-')[1:-1] # '(5,4,3)' -> '5-4-3'
