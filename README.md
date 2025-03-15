# OLT AUTOMATE  

**Finalidade do Projeto**  

Este projeto é uma ferramenta desenvolvida em Python para facilitar a configuração de OLTs (Optical Line Terminals) da ZTE, mais especificamente os modelos C300, C320 e C350. A ferramenta tem como objetivo proporcionar um processo simplificado e intuitivo para a configuração dessas unidades, tornando mais fácil o trabalho dos profissionais de TI e técnicos de redes que precisam configurar essas OLTs, seja de forma inicial ou para manutenção

## Funcionalidades
O programa oferece um menu interativo que permite ao usuário selecionar diversas opções de configuração, de maneira clara e objetiva. Quando uma opção é escolhida, o programa retorna a configuração correspondente, além de fornecer explicações sobre a finalidade e os efeitos de cada configuração.

Como Salvar as Configurações
O programa orienta o usuário sobre como salvar as configurações feitas na OLT, garantindo que todas as alterações sejam persistentes após reinicializações.

Como Ativar e Desativar Interfaces
Esta opção permite que o usuário ative ou desative interfaces específicas da OLT, como interfaces de gerenciamento ou de uplink, diretamente pelo programa.

Verificação de Configurações Aplicadas
Ao selecionar essa opção, o usuário pode verificar as configurações que foram aplicadas na OLT, com a possibilidade de identificar se tudo está correto e funcionando como esperado.

Interfaces da OLT
O programa exibe detalhes sobre as interfaces configuradas na OLT, como informações sobre interfaces físicas e lógicas (PON, GPON, GEI), possibilitando um controle mais preciso das conexões.

•PNP das Placas na OLT:
Com essa opção, o usuário pode habilitar a detecção Plug-and-Play das placas e configurar o tipo de chassi, racks e shelves, facilitando a integração de novos módulos.

•Configuração de IP de Acesso:
Aqui, é possível configurar um novo IP de acesso para a OLT, permitindo que o gerenciamento remoto seja feito de forma eficiente.

•Configuração de Gateway Padrão:
A opção de configurar o gateway padrão é essencial para garantir que a OLT consiga se comunicar com outros dispositivos na rede, direcionando o tráfego de forma adequada.

•Configuração de VLAN de Gerência:
O programa permite configurar a VLAN de gerenciamento da OLT, o que é crucial para isolar o tráfego administrativo e garantir a segurança da rede.

•Configuração de Interface de Up-Link:
A interface de uplink (GEI) é configurada para permitir o tráfego de dados para a rede externa, incluindo a ativação de VLANs e ajustes de link.

•Acesso Remoto da OLT:
O usuário pode configurar o acesso remoto à OLT via Telnet ou SSH, garantindo o gerenciamento da OLT sem a necessidade de uma conexão física.

•Configuração de Banda:
Para otimizar a utilização da rede, essa opção configura o perfil de banda (TCON e tráfego), estabelecendo as bandas mínimas e máximas para os diferentes tipos de tráfego.

•Configuração de VLAN para ONU:
Essa funcionalidade permite configurar a VLAN para a ONU, permitindo que as ONUs se comuniquem na rede corretamente com a OLT.

•Acesso Remoto da ONU:
Similar ao acesso remoto da OLT, essa opção configura o acesso remoto das ONUs, garantindo que possam ser gerenciadas sem necessidade de intervenção local.

•Configuração de PPPOE, Rede e Senha da ONU:
O PPPOE pode ser configurado, juntamente com a rede e a senha de cada ONU, permitindo a autenticação e conectividade com a rede.

•Histórico das Configurações Aplicadas:
O programa mantém um histórico das configurações que foram aplicadas, o que permite um acompanhamento das ações feitas até o momento e facilita a revisão do que foi alterado.

•Reset da OLT:
Permite realizar um reset completo da OLT, útil em situações de erro ou para voltar as configurações para os padrões de fábrica.

•Backup das Configurações da OLT:
O backup das configurações da OLT é fundamental para preservar as configurações e poder restaurá-las facilmente em caso de falhas ou reconfiguração do dispositivo.  

## 📂 Usabilidade no dia-a-dia 

👉 O principal objetivo deste projeto é automatizar e simplificar o processo de configuração de OLTs ZTE, proporcionando um guia interativo para que qualquer técnico ou administrador de rede consiga configurar uma OLT desde o início sem a necessidade de decorar ou procurar cada comando manualmente.

A ferramenta tem a intenção de ser útil para iniciantes e profissionais experientes, permitindo uma configuração mais rápida, sem erros e com explicações claras para que o usuário compreenda o que está fazendo em cada etapa.

Além disso, este projeto também pode ser um ponto de partida para novas funcionalidades, como a integração com APIs para automação de tarefas ou a criação de interfaces gráficas para tornar o processo ainda mais acessível.
 
---


### **Menu de Configurações Iniciais**  
![Menu de Configurações Iniciais](https://github.com/user-attachments/assets/e4496a01-dea1-4f68-a035-fcca7ad2901a)  

### **Menu de Configurações de Nível Médio**  
![Menu de Configurações de Nível Médio](https://github.com/user-attachments/assets/1089cb06-5070-4046-83e2-398a15d3bfa8)  

### **Menu de Alto Nível**  
![Menu de Alto Nível](https://github.com/user-attachments/assets/3a25d5da-df01-443a-ba49-f2c02ec89476)  

### **Histórico Geral (Disponível Apenas Neste Menu)**  
![Histórico Geral](https://github.com/user-attachments/assets/c594ec5f-3044-4486-824d-4aab64e15d0f)  

### **Menu Extra (Opções de Subir ONU, etc.)**  
![Menu Extra](https://github.com/user-attachments/assets/9255ea3b-7c22-4a51-b88c-cf19df864de3)  

### **Menu de Backup e Reset**  
![Menu de Backup e Reset](https://github.com/user-attachments/assets/9256a656-a327-4246-a39f-ce122c59117d)  


---  

[**LinkedIn**](https://www.linkedin.com/in/delucas027)
