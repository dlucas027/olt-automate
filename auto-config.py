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

def add_config():
    name = input("Nome da configuração:Autorizar ONU")
    description = input("Descrição: Entrar na interface G-PON antes de autorizar")
    command = input("""Comando:
interface gpon-olt_?/?/?
    onu 1 type ZTE-F601 sn ZTEGCCE7B888
""")
    config = Config(name, description, command)
    configs.append(config)
    print("Configuração adicionada!")

def list_configs():
    for config in configs:
        print(config)

# Loop principal
while True:
    print("1. Listar configurações")
    print("2. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        add_config()
    elif opcao == "2":
        list_configs()
    elif opcao == "3":
        break
