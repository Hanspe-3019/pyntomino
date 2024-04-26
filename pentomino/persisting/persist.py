''' Persistierung eines Problems (gelöst oder ungelöst)
Benutzt shelve. Die Datenbank heißt pentomino.db in dem Verzeichnis
laut $SELVEDIR.
Ist $SELVEDIR nicht gesetzt, landet es im home directory.
'''
import os
from pathlib import Path
import shelve
import dbm

from pentomino.problems import build

DB = os.environ.get('SHELVEDIR', Path.home() ) / 'pentomino-n'

USER = '#'

def store_solution(solution):
    ''' sha1 + '_' + lfd
    '''
    trimmed = build.trim_with_empty_hull(solution)
    trimmed[trimmed > 0] = 0
    its_hash = build.hash_it(trimmed)
    with shelve.open(DB, flag='c') as db:
        try:
            cnt = max(
                version_as_int(key) for key in db.keys()
                if key.startswith(its_hash)
            )
        except ValueError: # keys() is empty
            cnt = 0
        else:
            cnt += 1

        key = f'{its_hash}_{cnt}'
        db[key] = solution

    return key

def store_problem(problem):
    ''' USER + sha1
    '''
    its_hash = build.hash_it(problem)
    with shelve.open(DB, flag='c') as db:

        key = f'{USER}{its_hash}'
        db[key] = problem
    return key

def version_as_int(key):
    ' xxxxx_yy_nnn -> int(nnn)'
    version = key.rsplit('_', maxsplit=1)[1]
    return int(version)

def get_versions(prefix):
    ' -> sorted( (k, v) ) '
    try:
        with shelve.open(DB, flag='r') as db:
            return sorted(
                (
                    (key, val) for key, val in db.items() if key.startswith(prefix)
                )
            )
    except dbm.error:
        return []

def get_keys(prefix='', suffix=''):
    ''' startswith('') and .endwith('') always true
    '''
    try:
        with shelve.open(DB, flag='r') as db:

            return [
                key for key in db.keys()
                if key.startswith(prefix) and key.endswith(suffix)
            ]
    except dbm.error:
        return []

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

def to_menulabel(key):
    ''' -
    '''
    if key.startswith(USER):
        # '#' + SHA1 + '_0' -> die ersten 10 Halbbytes von SHA1
        return key[1:11]

    return key
