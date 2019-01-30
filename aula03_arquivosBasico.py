arquivo = open("aula03_arquivoTeste.txt","w")

arquivo.write("-Olá mundo.\n -Olá\n")

arquivo.close()

arquivo = open("aula03_arquivoTeste.txt","r")

linha_do_arquivo = arquivo.readline()

print("Conteúdo do arquivo:",linha_do_arquivo)

arquivo.close()
