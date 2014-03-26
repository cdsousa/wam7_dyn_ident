import sys
import sympy

def _fprint(x):
    print(x)
    sys.stdout.flush()

def mrepl(m,repl):
  return m.applyfunc(lambda x: x.xreplace(repl))

def skew(v):
  return sympy.Matrix( [ [     0, -v[2],  v[1] ],
                         [  v[2],     0, -v[0] ],
                         [ -v[1],  v[0],     0 ] ] )

class ListTable(list):
    """ Overridden list class which takes a 2-dimensional list of 
        the form [[1,2,3],[4,5,6]], and renders an HTML Table in 
        IPython Notebook. """
    
    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")
            
            for col in row:
                html.append("<td>{0}</td>".format(col))
            
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
