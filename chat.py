import os

mensagens = []

nome = input ("Nome: ")

while True:
    
    #limpando o terminal
    os.system('cls')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print (m["nome"], "-", m["texto"])
            
    print("______________________")
    
#obtendo texto
    texto = input ("Mensagem: ")
    if texto == "fim":
        break

#adicionando mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
    
    
print("Encerrando chat")
    