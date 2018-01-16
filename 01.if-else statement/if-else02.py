page='tv'
bc = 'on' if page=='tv' else 'off'
print bc

bc = ('start','stop')[page=='tv']
print bc

want_bc = {True: 'on', False: 'off'}
bc = want_bc[page == 'tv']
print bc
