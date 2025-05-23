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
DBVERSION = None

USER = '#'

def store_solution(solution):
    ''' sha1 + '_' + lfd
    '''
    its_hash = build.hash_of_problem(solution)

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
    its_hash = build.hash_of_problem(problem)
    with shelve.open(DB, flag='c') as db:

        key = f'{USER}{its_hash}'
        db[key] = problem
    return key

def version_as_int(key):
    ' xxxxx_yy_nnn -> int(nnn)'
    version = key.rsplit('_', maxsplit=1)[1]
    return int(version)

def get_solutions(hash_problem):
    ' -> sorted( (k, v) ) '
    try:
        with shelve.open(DB, flag='r') as db:
            prefix = hash_problem.removeprefix(USER)
            solutions = sorted(
                (
                    (key, val) for key, val in db.items()
                    if key.startswith(prefix)
                )

            )
            return solutions
    except dbm.error:
        return []

def has_problems_user():
    ' - '
    try:
        with shelve.open(DB, flag='r') as db:
            any_key = (key for key in db.keys() if key.startswith(USER))
            return next(any_key, False) is not False
    except dbm.error:
        return False

def get_problems_user():
    ' USER + sha1 '
    try:
        with shelve.open(DB, flag='r') as db:

            return [
                key for key in db.keys() if key.startswith(USER)
            ]
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
