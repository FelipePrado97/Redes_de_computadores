import socket, struct , os, sys, shutil

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8888))
full_msg = ''
while True:
    new_msg = True
    while True:
        msg = s.recv(1024)
        full_msg+= msg.decode("utf-8")
        
        print(full_msg)
        op = input("Escolha uma opção>")
        while op != '6':
            if op == '1':
                s.send(bytes(op,"utf-8"))
                resposta1 = s.recv(2048).decode("utf-8")
                print(resposta1)
                
                escolha1 = input("Diretorio: ")
                s.send(bytes(escolha1,"utf-8"))
                
                resposta3 = s.recv(2048).decode("utf-8")
                print(resposta3)

                print(full_msg)
                op = input("Escolha uma opção>")
            elif op == '2':
                s.send(bytes(op,"utf-8"))
                resposta1 = s.recv(2048).decode("utf-8")
                print(resposta1)
                
                escolha1 = input("Diretorio: ")
                s.send(bytes(escolha1,"utf-8"))
                
                resposta3 = s.recv(2048).decode("utf-8")
                print(resposta3)

                print(full_msg)
                op = input("Escolha uma opção>")
            elif op == '3':
                s.send(bytes(op,"utf-8"))
                                
                p = ' '
                g = input("Informe diretorio ou aperte enter para continuar: ")
                p += g
                if p == ' ':
                    s.send(bytes(p,"utf-8"))
                else:
                    s.send(bytes(g,"utf-8"))
                 
                resposta2 = s.recv(2048).decode("utf-8")
                print(resposta2)
                print("\n\n")
                print(full_msg)
                op = input("Escolha uma opção>")
            elif op == '4':
                s.send(bytes(op,"utf-8"))
                caminho = input("Informe o caminho do arquivo a ser enviado!   > ")
                nome = input("Informe o Nome do Arquivo, Ex: teste.txt   >  ")
                path1 = caminho + '\\' + nome

                while os.path.exists(path1) != True:
                    print("Arquivo nao encontrado")
                    caminho = input("Informe o caminho do arquivo a ser enviado!   > ")
                    nome = input("Informe o Nome do Arquivo, Ex: teste.txt   >  ")
                    path1 = caminho + '\\' + nome

                s.send(bytes(nome,"utf-8"))

                diretorios = s.recv(2048).decode("utf-8")
                print(diretorios)

                
                
                p = ' '
                g = input("Informe diretorio ou aperte enter para continuar: ")
                p += g
                s.send(bytes(p,"utf-8"))
                if p == ' ':
                    resultado = s.recv(2048).decode("utf-8")
                    if resultado == "falha":
                        print("Nome do arquivo já existe, renomeie ou envie para outro diretorio!")
                    else:
                        if os.path.exists(path1):
                            with open(path1, 'rb') as file:
                                data = file.read()
                                s.send(data)
                        else:
                            print("Arquivo não encontrado")
                else:
                    s.send(bytes(g,"utf-8"))
                    resultado = s.recv(2048).decode("utf-8")
                    if resultado == "falha":
                        print("Nome do arquivo já existe, renomeie ou envie para outro diretorio!")
                    else:
                        if os.path.exists(path1):
                            with open(path1, 'rb') as file:
                                data = file.read()
                                s.send(data)
                        else:
                            print("Arquivo não encontrado")
                resultado = s.recv(2048).decode("utf-8")
                print(resultado)
                print(full_msg)
                op = input("Escolha uma opção>")          
                
            elif op == '5':
                s.send(bytes(op,"utf-8"))
                
                caminho = input("Informe caminho ou aperte enter para continuar: ")
                nome = input("Informe nome do arquivo a ser removido! Ex: teste.txt: >")

                if caminho != '':
                    path = caminho + '\\' + nome
                else:
                    path = nome
                
                s.send(bytes(path,"utf-8"))
                resposta3 = s.recv(2048).decode("utf-8")
                print(resposta3)

                print(full_msg)
                op = input("Escolha uma opção>")
            
            else:
                print("Opção incorreta! ")
                print(full_msg)
                op = input("Escolha uma opção>")

        if op == '6':
            print("Fim de Conexão")
            s.close()
            