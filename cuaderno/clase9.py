'''
lista=[]
archivo=open('V:\Course Python\cuaderno\devices.txt')
for item in archivo:
    #item=item.strip()
    #item=item.upper()
    item=item.strip('Cisco')
    lista.append('item')
    print(item)
archivo.close
print(lista)
'''
archivo=open('V:\Course Python\cuaderno\devices.txt','a')
while True:
    nitem = input('')
    if nitem == 'salir':
        print('esta hecho')
        break
    archivo.write(nitem + '\n')
archivo.close()
    