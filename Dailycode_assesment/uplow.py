def swap(pYTHON):
    st=''
    for i in 'pYTHON':
        if i.islower() == True:
            st = st+i.upper()
        else:
            st=st+i.lower()
    return st


print(swap('pYTHON'))