'''
datos=100
nativa=1
if datos==nativa:
    print('los vlan son iguales')
else:
    print('los vlan son diferentes')
    '''
"""
acl=int(input('ingrese el # de ACL:'))
if acl>=1 and acl<=99:
    print('es una acl estandar')
elif acl>=100 and acl<=199:
    print('es una acl extendida')
else:
    print('el # ingresado no es acl')
    """

"""   
lista=[1,251,984,25468,87659,7781]
for item in lista:
    print(item)

for i in range(1,10+1,1):
    print(i,end=' * ')
    """

lista=['r1','r2','r3','s1','s2','s3','API1','API2','API3']
for elemento in lista:
    if 'r' in elemento:
        print('elemento')