''' Utility: Scan pentomino.db
'''
import shelve
from collections import defaultdict

from pentomino import persist

print(persist.DB)

def scan():
    ' - '
    groups = defaultdict(list)
    to_be_checked = []

    with shelve.open(persist.DB, 'r') as db:
        for key in sorted(db.keys()):
            try:
                obj = db.get(key)
                obj_type = obj.__class__.__name__
                try:
                    obj_type += f'{obj.shape}'
                    group = get_group(key)
                    if group is not None:
                        groups[group].append( (key, obj.shape) )
                    else:
                        to_be_checked.append((key, obj_type))
                except AttributeError:
                    to_be_checked.append(key)
            except ModuleNotFoundError as xcptn:
                to_be_checked.append(key)
                obj_type = xcptn.name
                obj = None
            # End for loop

        print('# Grouped:')
        for group in groups:
            print(f'{group:20s}: {len(groups[group]):5d}')
        if len(to_be_checked) > 0:
            print('# to be checked:')
            for key in to_be_checked:
                print(f'? {key}')


def get_group(key):
    ''' -
    '''
    try:
        group, num = key.rsplit('_', maxsplit=1)
        num = int(num)
    except ValueError:
        return None

    if key.startswith(persist.USER) and len(key) != 40 + 3:
        return None
    return persist.to_menulabel(group)
