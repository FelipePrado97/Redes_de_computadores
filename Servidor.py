import socket, struct , os, sys, shutil

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',8888))
s.listen()
print("Aguardando Conexão com o Cliente")

while True:
    clientsocket, address = s.accept()
    print(f"Conectado em {address}")
    msg ="[1] - Criar Diretório\n [2] - Remover Diretório\n [3] - Listar Conteúdo de Diretório\n [4] - Enviar Arquivo\n [5] - Remover Arquivo\n [6] - Sair"

    clientsocket.send(bytes(msg, "utf-8"))

    op = clientsocket.recv(1024).decode("utf-8")
    while op != '6':
        if op == '1':
            print ("[1] - Criar Diretório\n")
            
            clientsocket.send("Informe o Nome diretório> ".encode())#r2
            nome = clientsocket.recv(1024).decode("utf-8")
            
            try:
                os.mkdir(nome)
                rep = "Diretorio Criado com Sucesso ".encode()
            except OSError as error:
                rep = str(error).encode()
            
            clientsocket.send(rep)#r3
            op = clientsocket.recv(1024).decode("utf-8")
        elif op == '2':
            print ("[2] - Remover Diretório\n")
            
            clientsocket.send("Informe o Nome diretório> ".encode())#r2
            nome = clientsocket.recv(1024).decode("utf-8")
            
            nome
            try:
                shutil.rmtree(nome)
                rep = "Diretorio Removido com Sucesso ".encode()
            except OSError as error:
                rep = str(error).encode()
            
            
            clientsocket.send(rep)#r3
            op = clientsocket.recv(1024).decode("utf-8")
        elif op == '3':
            print ("[3] - Listar Conteúdo de Diretório\n")
            
            
            dire_loc = clientsocket.recv(1024).decode("utf-8") 
            if dire_loc == ' ':
                dirs = os.listdir()
                diretorios = ' '
                for file in dirs:
                    diretorios += '\n'+str(file)
            else:
                dirs = os.listdir(dire_loc)
                diretorios = ' '
                for file in dirs:
                    diretorios += '\n'+str(file) 
            clientsocket.send(diretorios.encode()) #r2         
                
            op = clientsocket.recv(1024).decode("utf-8")
             
        elif op == '4':
            print ("[4] - Enviar Arquivo\n")
            
            namefile = clientsocket.recv(1024).decode("utf-8")
            
            #enviar dires
            dirs = os.listdir()
            diretorios = ' '
            for file in dirs:
                diretorios += '\n'+str(file) 
            clientsocket.send(diretorios.encode())
            
            p = clientsocket.recv(1024).decode("utf-8")
            if p == ' ':
                if os.path.exists(namefile):
                    resultado = "falha"
                    clientsocket.send(resultado.encode())
                else:
                    resultado = "sucesso"
                    clientsocket.send(resultado.encode())
                    with open(namefile, 'wb') as file:
                        data = clientsocket.recv(1000000)
                        file.write(data)
                    resultado= "Enviou arquivo"
            else:
                g = clientsocket.recv(1024).decode("utf-8")
                namefile = g + '/'+ namefile
                if os.path.exists(namefile):
                    resultado = "falha"
                    clientsocket.send(resultado.encode())
                else:
                    resultado = "sucesso"
                    clientsocket.send(resultado.encode())
                    with open(namefile, 'wb') as file:
                        data = clientsocket.recv(1000000)
                        file.write(data)
                    resultado = "Enviou arquivo"

            clientsocket.send(resultado.encode())
            op = clientsocket.recv(1024).decode("utf-8")
        elif op == '5':
            print ("[5] - Remover Arquivo\n")
            
            path = clientsocket.recv(1024).decode("utf-8")
                        
            if os.path.exists(path):
                try:
                    os.remove(path)
                    rep = "Arquivo Removido com Sucesso!".encode()
                    clientsocket.send(rep)#r3 
                except OSError as error:
                    rep = str(error).encode()
            else:
                rep = "Arquivo Não Encontrado! ".encode()
                clientsocket.send(rep)#r3 
            
            op = clientsocket.recv(1024).decode("utf-8")
        else:
            clientsocket.send("Opção Incorreta".encode())
            op = clientsocket.recv(1024).decode("utf-8")