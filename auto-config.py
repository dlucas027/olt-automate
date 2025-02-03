class Config:
    _id_counter = 1

    def __init__(self, name, description, command):
        self.code = Config._id_counter
        Config._id_counter += 1
        self.name = name
        self.description = description
        self.command = command

    def __str__(self):
        return f"[Cód: {self.code}] {self.name} - {self.description}\n{self.command}\n"


configs = []  # Lista de configurações

class Config:
    def __init__(self, name, description, command):
        self.name = name
        self.description = description
        self.command = command

    def __str__(self):
        return f"Nome: {self.name}\nDescrição: {self.description}\nComando: {self.command}\n"


configs = []  # Lista de configurações
def add_authorize_onu():
    name = input("Nome da configuração: Autorizar ONU")
    description = input("Descrição: Entrar na interface G-PON antes de autorizar")
    command = input("""Comando:
interface gpon-olt_?/?/?
    onu 1 type ZTE-F601 sn ZTEGCCE7B888
""")
    config = Config(name, description, command)
    configs.append(config)
    print("Último Comando: Autorizar ONU!")  


def add_enable_pon():
    name = input("Nome da configuração: Habilitar PON")
    description = input("Descrição: Entrar na interface G-PON para habilitar, selecione a PON específica")
    command = input("""Comando:
interface gpon-olt_1/1/1
  show this
  shutdown (DESATIVADA)
  linktrap disable
""")
    config = Config(name, description, command)
    configs.append(config)
    print("Último Comando: Autorizar ONU!") 

def add_script_vsol():
    name = input("Nome da configuração: Script VSOL")
    description = input("Descrição: Entrar na interface PON, Modelo de Script para VSOL")
    command = input("""Comando:
onu-type VSOL-BRIDGE-1P gpon
onu-type VSOL-BRIDGE-1P gpon max-tcont 8
onu-type VSOL-BRIDGE-1P gpon max-gemport 32
onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
onu-type VSOL-BRIDGE-1P gpon max-iphost 5
onu-type-if VSOL-BRIDGE-1P eth_0/1
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Script VSOL' executado com sucesso!")  

def add_script_F601():
    name = input("Nome da configuração: Script ZTE-F601")
    description = input("Descrição: Entrar na interface PON, Modelo de Script para ZTE-F601")
    command = input("""Comando:
onu-type ZTE-F601 gpon
onu-type ZTE-F601 gpon max-tcont 8
onu-type ZTE-F601 gpon max-gemport 32
onu-type ZTE-F601 gpon max-switch-perslot 8
onu-type ZTE-F601 gpon max-flow-perswitch 8
onu-type ZTE-F601 gpon max-iphost 5
onu-type-if ZTE-F601 eth_0/1
""")
    config = Config(name, description, command)
    configs.append(config)
    print("'Script ZTE-F601' executado com sucesso!")  


# Loop principal
while True:
    print("1. Autorizar ONU")
    print("2. Habilitar PON")
    print("3. Script VSOL")
    print("4. Script ZTE-F601")
    print("5. Sair")  # A opção de sair estava com o símbolo errado
    opcao = input("Escolha: ")

    if opcao == "1":
        add_authorize_onu()   # Chama a função para adicionar "Autorizar ONU"
    elif opcao == "2":
        add_enable_pon()      # Chama a função para adicionar "Habilitar PON"
    elif opcao == "3":
        add_script_vsol()     # Chama a função para adicionar "Script VSOL"
    elif opcao == "4": 
        add_script_F601()     # Chama a função para adicionar "Script F601"
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")



