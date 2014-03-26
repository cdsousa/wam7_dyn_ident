
from sympy import latex
import numpy

def baseparms_pretty_latex(delta,Pb,Pd,Kd):
    base_latex = []
    delta_b = Pb.T * delta
    delta_d = Pd.T * delta
    n_b = len(delta_b)
    n_d = len(delta_d)
    for i in range(n_b):
        _latex = latex( delta_b[i] )
        l = []
        for j in range(n_d):
            c = Kd[i,j]
            if c == -1 or c == 1:
                _latex += ' ' + ('+ ' if c > 0 else'') + latex( c * delta_d[j] )
            elif c != 0 and j not in l:
                ll = []
                for jj in range(j,n_d):
                    cc = Kd[i,jj]
                    if cc == c:
                        l.append(jj)
                        ll.append(delta_d[jj])
                p = (' \, ( ',' ) ') if (len(ll) > 1) else (' \, ','')
                ll_sum = ' + '.join( [ latex( lli ) for lli in ll] )
                _latex += ' ' + ('+ ' if c > 0 else'') + latex( c.n() ) + p[0] + ll_sum + p[1]
        base_latex.append(_latex)
    return base_latex;


def unpack_a_b_q0(a_b_q0,dof):
    L = (len(a_b_q0)-dof) / (dof*2)
    ail = numpy.zeros((dof,L))
    bil = numpy.zeros((dof,L))
    q0i = numpy.zeros(dof)
    for i in range(dof):
        for l in range(L):
            ail[i,l] = a_b_q0[l+i*L]
            bil[i,l] = a_b_q0[l+i*L+dof*L]
        q0i[i] = a_b_q0[i+dof*L*2]
    return ail,bil,q0i

def latextable_a_b_q0(a_b_q0,dof):
    L = (len(a_b_q0)-dof) / (dof*2)
    ail,bil,q0i = unpack_a_b_q0(a_b_q0,dof)
    s = '\\begin{tabular}{crrrrr}\n'
    s += '\\toprule\n'
    s += 'Joint $k$'
    for l in range(L):
        s += ' & $a_{k,%i}$'%(l+1)
    s += ' \\\\\n\\cmidrule(lr){2-%i}\n'%(L+1)
    for i in range(dof):
        s += '$%i$'%(i+1)
        for l in range(L):
            s += ' & $%.2f$'%ail[i,l]
        s += ' \\\\\n'
    s += '\\end{tabular}\n'
    s += '\\begin{tabular}{crrrrrr}\n'
    s += '\\midrule\n'
    s += '$k$'
    for l in range(L):
        s += ' & $b_{k,%i}$'%(l+1)
    s += ' & $q_{k,0}$'
    s += ' \\\\\n\\cmidrule(lr){2-%i}\n'%(L+2)
    for i in range(dof):
        s += '$%i$'%(i+1)
        for l in range(L):
            s += ' & $%.2f$'%bil[i,l]
        s += ' & $%.2f$'%(q0i[i])
        s += ' \\\\\n'
    s += '\\bottomrule\n'
    s += '\\end{tabular}\n'
    return s