def menu_backreset():
    print("="*55)
    print(" " * 5 + "BACKUP E RESET, OLT ZTE C300, C320 E C350" + " " * 10)
    print("="*55)
    print("[1] - RESET")
    print("[2] - BACKUP")
    print("[3] - SAIR")
    print("="*55)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

while True:
    opcao = menu_backreset()

    if opcao == "1":
        print("""RESET:
file delete cfg-startup *.*
yes
reboot
yes""")
    
    elif opcao == "2":
        print("""RESET:

•Usando Mikrotik, vamos encontrar o arquivo de backup, para darmos o comando na OLT.

MIKROTIK > SYSTEM > USERS 
                        ATIVAR PORTA FTP
                        FILE LIST0 (ARQUIVO DE BACKUP DA OLT)
            
TERMINAL DA OLT:
                file upload cfg-startup *.* ftp ipaddress  [IP de FTP] user [USUÁRIO] password [SENHA]
""") 
    elif opcao == "3":
        print("Cuidado com as configurações de reset e backup...até logo!")
        break