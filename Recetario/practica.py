mi_texto = open('registro.txt','a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for l in registro_ultima_sesion:
    mi_texto.writelines(l+ '\t')
mi_texto.close()
mi_texto = open('registro.txt')
print(mi_texto.read())