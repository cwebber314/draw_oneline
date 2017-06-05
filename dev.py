r"""
Play around with SchemDraw

To use in Jupyter Notebook:

    %matplotlib inline
    %config InlineBackend.figure_format = 'svg'

"""
import oneline_elements as onl
import SchemDraw as schem

d = schem.Drawing()
bb.add_label('A', loc='top')
bb.add_label('105', loc='bot')
d.draw()
