arquivo = open("teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["Escrevendo ", "um ", "novo ", "texto "]) # Escreve letra por letra

arquivo.close()