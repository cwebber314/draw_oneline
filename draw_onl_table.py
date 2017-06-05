"""
Draw oneline from a rather specific CSV table that describes a circuit.
"""
import csv
import os
import os.path as osp
from functools import partial

import SchemDraw as schem
import SchemDraw.elements as e
import oneline_elements as onl

def clean_csv(rows):
    """
    Sanity check CSV data and type cast
    """
    for i in range(len(rows)):
        rows[i]['loc'] = int(rows[i]['loc'])
    return rows

fn = 'oneline_table.csv'
reader = csv.DictReader(open(fn, 'r'))
rows = [row for row in reader]
rows = clean_csv(rows)

def get_rows(rows, which):
    """
    Get all the rows for the 1xx leg

    Args:
      - which (int): starting location.  Retrieve this location + 100.   This
        value should be [100, 200, 300]
    """
    new_rows = []
    for row in rows:
        if row['loc'] >= which and row['loc'] < (which + 100):
            new_rows.append(row)
    return new_rows

def identify_layout(rows):
    """
    Return layout of branch.  Possible values are 'single', 'double'
    """
    locs = [row['loc'] for row in rows]
    max_loc = max(locs)
    if max_loc > 300:
        layout = 'double'
    else:
        layout = 'single'
    return layout

def draw_leg(d, rows, start_loc=None, direction=None):
    """
    Draw one leg of the oneline.

    Args:
     d (SchemDraw.Drawing): Drawing object
     rows (list): list of dictionaries of items to draw
     start_loc (tuple): location to start drawing.  Example (0,0)
     direction (str): direction to start draw.  Valid values are
       [left, right, up, down]

    Returns:
      SchemDraw.Drawing: Update drawing
    """

    sorted_rows = sorted(rows, key=lambda k: k['loc'])
    len_ct = 2*0.75
    # Draw a simple line to get everything start off in the right direction
    d.add(e.LINE, l=0.1, d=direction, xy=start_loc)
    for row in sorted_rows:
        alpha = row['alpha']
        loc = str(row['loc'])
        if row['element'] == 'subcond':
            ee = d.add(onl.SUBCOND, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        elif row['element'] == 'wavetrap':
            ee = d.add(onl.WAVETRAP, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        elif row['element'] == 'breaker':
            ee = d.add(onl.BREAKER, l=len_ct, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        elif row['element'] == 'switch':
            ee = d.add(onl.SWITCH, l=len_ct, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        elif row['element'] == 'CT':
            ee = d.add(onl.CT, l=len_ct, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        elif row['element'] == 'bus':
            ee = d.add(onl.BUS, d=direction)
            ee.add_label(alpha, loc='top')
            ee.add_label(loc, loc='bot')
        else:
            raise ValueError("Invalid Equipment Class")
    return d

leg1 = get_rows(rows, 100)
leg2 = get_rows(rows, 200)
leg3 = get_rows(rows, 300)

d = schem.Drawing(unit=2)
dot = d.add(e.DOT)
ee = d.add(e.LINE, d='up', l=4.5)
leg2_start = ee.end

d = draw_leg(d, leg1, start_loc=dot.start, direction='left')
d = draw_leg(d, leg2, start_loc=leg2_start, direction='left')
d = draw_leg(d, leg3, start_loc=dot.start, direction='right')

d.draw(showplot=False)
d.save('table_oneline.svg')
d.save('table_oneline.png')
