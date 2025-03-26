# automateOLT  

---

## Project Purpose

This project is a tool developed in Python to facilitate the configuration of ZTE Optical Line Terminals (OLTs), specifically the C300, C320, and C350 models. The tool aims to provide a simplified and intuitive process for configuring these units, making it easier for IT professionals and network technicians to configure these OLTs, whether for initial setup or for maintenance.

## Features
The program offers an interactive menu that allows the user to select various configuration options, in a clear and objective way. When an option is selected, the program returns the corresponding configuration, along with explanations about the purpose and effects of each configuration.

### How to Save Configurations
The program guides the user on how to save the settings made on the OLT, ensuring that all changes persist after reboots.

### How to Activate and Deactivate Interfaces
This option allows the user to activate or deactivate specific interfaces on the OLT, such as management or uplink interfaces, directly from the program.

### Verifying Applied Configurations
By selecting this option, the user can verify the configurations that have been applied on the OLT, with the possibility of checking if everything is correct and functioning as expected.

### OLT Interfaces
The program displays details about the configured interfaces on the OLT, including information about physical and logical interfaces (PON, GPON, GEI), providing more precise control over the connections.

### PNP of the OLT Cards:
With this option, the user can enable Plug-and-Play detection of cards and configure the chassis type, racks, and shelves, facilitating the integration of new modules.

### Access IP Configuration:
Here, the user can configure a new access IP for the OLT, allowing efficient remote management.

### Default Gateway Configuration:
The option to configure the default gateway is essential to ensure that the OLT can communicate with other devices on the network, routing traffic appropriately.

### Management VLAN Configuration:
The program allows the configuration of the OLT's management VLAN, which is crucial to isolate administrative traffic and ensure network security.

### Up-Link Interface Configuration:
The uplink interface (GEI) is configured to allow data traffic to the external network, including VLAN activations and link adjustments.

### Remote OLT Access:
The user can configure remote access to the OLT via Telnet or SSH, ensuring OLT management without the need for a physical connection.

### Bandwidth Configuration:
To optimize network usage, this option configures the bandwidth profile (TCON and traffic), establishing minimum and maximum bandwidths for different types of traffic.

### VLAN Configuration for ONU:
This feature allows configuring the VLAN for ONUs, ensuring that ONUs can communicate properly on the network with the OLT.

### Remote Access for ONU:
Similar to remote OLT access, this option configures remote access for ONUs, ensuring they can be managed without local intervention.

### PPPOE Configuration, Network, and ONU Password:
PPPoE can be configured along with the network and password for each ONU, enabling authentication and connectivity with the network.

### History of Applied Configurations:
The program keeps a history of the configurations that have been applied, allowing tracking of actions taken and facilitating review of what has been altered.

### OLT Reset:
Allows performing a complete reset of the OLT, useful in error situations or to revert the settings to factory defaults.

### OLT Configuration Backup:
Backing up the OLT's configurations is essential to preserve the settings and easily restore them in case of failure or device reconfiguration.  

---

## 📂 Usability in Daily Life

The main objective of this project is to automate and simplify the process of configuring ZTE OLTs, providing an interactive guide so that any technician or network administrator can configure an OLT from scratch without the need to memorize or search for each command manually.

The tool aims to be useful for both beginners and experienced professionals, enabling faster configurations without errors and with clear explanations so the user understands what they are doing at each step.

Furthermore, this project could also serve as a starting point for new features, such as integration with APIs for task automation or the creation of graphical interfaces to make the process even more accessible.

---

## Project Features

The code has been refactored, and now in the "refactor" folder, you can find all configurations in one place.
Additionally, it has been integrated with a graphical interface, as initially desired in the project.

### **Configuration Menu**  
![Configuration Menu](https://github.com/user-attachments/assets/28efe1bf-2d12-4e6c-9244-1f2fd442e132)
  

### **Project in Action**  
![Project in Action](https://github.com/user-attachments/assets/83e4808c-a206-40f2-b82a-f2e67b0ba51f)
  

### **Example of Returned Command**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/11b9eb6d-9ce0-4d0d-938a-81c810d1d1af" alt="Example of Returned Command" />
</p>


---
---
---

[**LinkedIn**](https://www.linkedin.com/in/delucas027)
