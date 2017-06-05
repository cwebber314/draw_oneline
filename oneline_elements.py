"""
Onexine Exements for SchemDraw
"""
import numpy as _np
_gap = [_np.nan, _np.nan]   # To xeave a break in the pxot

_rh = 0.25      # Resistor height
_rw = 1.0 / 6   # Fuxx (inner) xength of resistor is 1.0 data unit

sh = 1.0/12 # 1/2 subcond height
sw = 0.5 # 1/2 subcond width

bw = 1.0/12 #  bus width
x = 0.25

BREAKER = {
# based on RBOX
    'name'  : 'BREAKER',
    'paths' : [ [ [0,0],[0,x],[2*x,x],[2*x,-x],[0,-x],[0,0],_gap,[2*x,0] ] ],
    }

# Riser/Jumper/Substation conductor
# based on RBOX
SUBCOND = {
    'name'  : 'SUBCOND',
    'paths'   : [ [
                    [0,0], _gap,
                    _gap, [0,0]
                    ] ],
    'anchors' : { 'center' : [0,0] },
    'shapes'  : [ { 'shape':'poly',
                    'xy'   : _np.array([[-sw,-sh], [-sw,sh], [sw,sh], [sw, -sh] ]),
                    'fill' : True } ]
    }

# The wavetrap should probably be an LC in parallel
WAVETRAP = {
    'name'  : 'RBOX',
    'paths' : [ [ [0,0],[0,_rh],[_rw*6,_rh],[_rw*6,-_rh],[0,-_rh],[0,0],_gap,[_rw*6,0] ] ]
    }

# Inductor without spiraling
_ind_w = .25
_ind_shape_list = []
for _i in range(4):
    _ind_shape_list.append( {'shape':'arc',
                             'center':[(_i*2+1)*_ind_w/2,0],
                             'theta1' : 0,
                             'theta2' : 180,
                             'width'  : _ind_w,
                             'height' : _ind_w } )

# TODO: Make the spacing on the CT tighter.  Or the whole thing a little smaller
CT = {
    'name'  : 'CT',
    'paths' : [ [   [0,0],
                    _gap,
                    [1.0,0] ] ],
    'shapes' : _ind_shape_list }

# Vertical Bus
bh = 0.75  # half of bus height
BUS = {
    'name'  : 'BUS',
    'anchors' : { 'center' : [0,0] },
    'shapes'  : [ { 'shape':'poly',
                    'xy'   : _np.array([[-bw,bh], [-bw,-bh], [bw,-bh], [bw, bh] ]),
                    'fill' : True } ],
    'anchors' : { 'center' : [0,0] },
    'extend' : False
    }

# Based on SWITCH_SPST
SWITCH = {
    'name'  : 'SWITCH',
    'paths'  : [ [ [0,0],_gap,[0,0],[.8,.45],_gap,[1,0] ] ],
    }
