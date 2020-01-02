#!/usr/bin/env python
# -*- coding: utf-8 -*-


def programa():
    def organizador():
        if comando == "wp":
            webPrincipal()
        elif comando == "it":
          tempseries

    def webPrincipal():
        titulo = input("Titulo: ")
        subtitulo = input("Subtitulo :")
        nSeries = int(input("Numero de serie a añadir"))
        total = '''<html>
<head><title>series</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
 
<h1>''' + titulo + '''</h1>
<h2>''' + subtitulo + '''</h2>
'''
        for i in range(0, nSeries):
            bl = input("boton o link: ")
            if bl == ('b' or 'B'):
                directorio = input("Directorio: ")
                Nserie = input("Nombre de la serie: ")
                total = total + '''
<button onclick="window.open(' ''' + directorio + ''' ', '_self')">''' + Nserie + '''</button> <br><br>
				'''

            elif bl == ('l' or 'L'):
                directorio = input("Directorio: ")
                Nseries = input("Nombre de la serie: ")
                total = total + '''<a href="''' + directorio + '''">''' + Nseries + '''</a><br><br>'''
        print(total + '''
</body></html>''')

    print('''
  Para crear una pagina principal usar --wp--,
  Para crear un indice de temporadas de una series --it--. 
  Para crear una lista de capitulos --lp--.
  Para crear el capitulo --cp--''')
    comando = " "
    comando = input("Que quieres crear: ")
    print(comando)
    organizador()


programa()
