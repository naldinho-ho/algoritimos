

# # ====== Menu Principal ======
# # 1. Armazenar as Palavra?
# # 2. Listar os Nomes
# # 3. Começar o Jogo
# # 4. Sair
# # Observação: Se o usuário informar uma opção inválida, apresente uma
# mensagem informando isso.

opcao=0
while opcao!=4:
	print("====== Menu Principal ======")
	print(" 1. Armazenar as Palavra")
	print(" 2. Listar os Nomes")
	print(" 3. Começar o Jogo")
	print(" 4. Sair")
	opcao=int(input("Digite sua opção: "))
	if opcao==1:
    	op1 = open("arquivos/nomes.txt", "a"))
    if nome = input("Informe seu nome completo: ")
		op1.write(nome)
		op1.write("\n")
		print("Fechando o arquivo...")
		op1.close()
    #
    #     	print("Ele é par!")
    # 	else:
    #     	print("Ele é impar")
	# if opcao==2:
    # 	op2x=int(input("Digite o valor para o número base x: "))
    # 	op2y=int(input("Digite o valor da potencia dele: "))
    # 	print("O resultado da", op2x, "elevado a", op2y,"É igual a:", op2x**op2y)
	# if opcao==3:
    # 	op3=int(input("Digite o valor do número que quer saber a raiz quadrada"))
    # 	print("O resultado é:", op3**(1/2))
	# if opcao==4:
    # 	print ("Finalizando...")
	# else:
    # 	print("Opção Inválida")
