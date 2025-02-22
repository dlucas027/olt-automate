def menu_exconfig():
    print("="*60)
    print(" " * 5 + "CONFIGURAÇÕES EXTRAS, OLT ZTE C300, C320 E C350" + " " * 10)
    print("="*60)
    print("[1] - ATIVAÇÃO DE PON")
    print("[2] - AUTORIZAR ONU")
    print("[3] - SCRIPTS DE ONU\ONT")
    print("[4] - SAIR")
    print("="*60)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

while True:
    opcao = menu_exconfig()

    if opcao == "1":
        print("""ATIVAÇÃO DE PON:
interface gpon-olt_1/1/1
show this
shutdown (DESATIVADA)
linktrap disable

no shutdown (ATIVADA)
exit
write
""")
    elif opcao == "2":
        print("""AUTORIZAR ONU:
interface gpon-olt_1/17/12
onu [NÚMERO DA ONU] type [MODELO] sn [MAC]    (onu 1 type ZTE-F601 sn ZTEGCCE7B888)
""")
    elif opcao == "3":
        print("""MODELO DE SCRIPT PARA ONU VSOL:
onu-type VSOL-BRIDGE-1P gpon
onu-type VSOL-BRIDGE-1P gpon max-tcont 8
onu-type VSOL-BRIDGE-1P gpon max-gemport 32
onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
onu-type VSOL-BRIDGE-1P gpon max-iphost 5
onu-type-if VSOL-BRIDGE-1P eth_0/1

MODELO DE SCRIPT PARA ONT ZTE-F660:
onu-type ZTE-F660 gpon
onu-type ZTE-F660 gpon max-tcont 8
onu-type ZTE-F660 gpon max-gemport 32
onu-type ZTE-F660 gpon max-switch-perslot 8
onu-type ZTE-F660 gpon max-flow-perswitch 8
onu-type ZTE-F660 gpon max-iphost 5

MODELO DE SCRIPT PARA ONU DLINK:
onu-type DLINK-MODELOX gpon
onu-type DLINK-MODELOX gpon max-tcont 8
onu-type DLINK-MODELOX gpon max-gemport 32
onu-type DLINK-MODELOX gpon max-switch-perslot 8
onu-type DLINK-MODELOX gpon max-flow-perswitch 8
onu-type DLINK-MODELOX gpon max-iphost 5

MODELO DE SCRIPT PARA ONU ZTE-F601:
onu-type ZTE-F601 gpon
onu-type ZTE-F601 gpon max-tcont 8
onu-type ZTE-F601 gpon max-gemport 32
onu-type ZTE-F601 gpon max-switch-perslot 8
onu-type ZTE-F601 gpon max-flow-perswitch 8
onu-type ZTE-F601 gpon max-iphost 5
onu-type-if ZTE-F601 eth_0/1
""")
    elif opcao == "4":
        print("Saindo...até breve!")
        break