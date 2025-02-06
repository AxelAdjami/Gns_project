# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:49:46 2025

@author: soufi
"""
"pour mettre a la suite de la ligne"
import os
import shutil
import json

# Chemins des répertoires pour 6 routeurs
repertoires_routeurs = {
    "routeur1": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/e35f8ed3-a75b-4a30-88ff-12400eba0a8a/configs",
    "routeur2": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/c0cc9e93-ad7d-4c30-ac16-093a5bfdffbe/configs",
    "routeur3": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/56b9b3bd-3752-45a2-a632-9f523af5267f/configs",
    "routeur4": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/736cb799-1726-41df-87fb-02ac5d27d134/configs",
    "routeur5": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/732d6a1a-5515-477b-806a-f5e5ddbf81e1/configs",
    "routeur6": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/66b35cb1-b286-4783-ba37-e801e027c01d/configs",
    "routeur7": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/3cec19c8-a9cb-4fa4-ac90-4627d450dc1d/configs",
    "routeur8": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/3016d222-7e7b-43da-89fd-72ea8b5e6f5a/configs",
    "routeur9": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/d46e0906-599b-4f18-af9b-765dfea48aeb/configs",
    "routeur10": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/8654fec2-b8bb-4f37-929e-2dd021bb12e4/configs",
    "routeur11": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/68c3204c-cea2-4e82-8fd7-64879e5f1e2c/configs",
    "routeur12": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/597a0de1-814d-48cf-ab2a-eb61978f80a7/configs",
    "routeur13": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/610baec9-f875-4e4e-9cf1-857ddfe5fa03/configs",
    "routeur14": "C:/Users/Axel/GNS3/projects/projet_final/project-files/dynamips/1910fb38-51b4-448a-b4ea-ca390838a438/configs",
}


repertoire_sources_config = "./"
suffixe_config = ".cfg"  # Extension des fichiers de configuration

def copier_configs_dans_repertoires(repertoires, repertoire_source):
    ""
    
    for routeur, rep_routeur in repertoires.items():
        nom_fichier_config = f"i{routeur[7:]}_startup-config.cfg"
        chemin_source = os.path.join(repertoire_source, nom_fichier_config)
        chemin_destination = os.path.join(rep_routeur, nom_fichier_config)

        # Vérifier si le répertoire du routeur existe
        if not os.path.exists(rep_routeur):
            print(f"Erreur : Le répertoire {rep_routeur} n'existe pas.")
            continue

        # Vérifier si le fichier de configuration existe
        if not os.path.exists(chemin_source):
            print(f"Avertissement : Le fichier {nom_fichier_config} n'existe pas dans {repertoire_source}.")
            continue

        # Copier le fichier de configuration
        try:
            shutil.copy(chemin_source, chemin_destination)
            print(f"Fichier {nom_fichier_config} copié dans {rep_routeur}.")
        except Exception as e:
            print(f"Échec de la copie de {nom_fichier_config} vers {rep_routeur} : {e}")




def ouvrir_json(fjson):
    # Charger le fichier JSON
    with open(fjson, 'r') as f:
        return json.load(f)

def append_to_configuration_line(file_path, marker, append_str):
    """
    Fonction pour ajouter des caractères à la fin d'une ligne spécifique dans un fichier de configuration.

    :param file_path: chemin du fichier de configuration.
    :param marker: une chaîne de caractères indiquant la ligne à modifier.
    :param append_str: chaîne de caractères à ajouter à la fin de la ligne trouvée.
    """
    # Lire le fichier et charger son contenu
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Parcourir chaque ligne pour trouver la ligne à modifier
    for i, line in enumerate(lines):
        if marker in line:  # Si le marqueur est trouvé dans la ligne
            lines[i] = append_str + "\n"  # Ajouter la chaîne à la fin de la ligne
    
    # Réécrire le fichier avec les modifications
    with open(file_path, 'w') as f:
        f.writelines(lines)

    print(f"Chaîne ajoutée à la fin de la ligne contenant '{marker}' dans {file_path}")

def append_to_configuration_line2(file_path, marker, append_str):
    """
    Fonction pour ajouter des caractères à la fin d'une ligne spécifique dans un fichier de configuration.

    :param file_path: chemin du fichier de configuration.
    :param marker: une chaîne de caractères indiquant la ligne à modifier.
    :param append_str: chaîne de caractères à ajouter à la fin de la ligne trouvée.
    """
    # Lire le fichier et charger son contenu
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Parcourir chaque ligne pour trouver la ligne à modifier
    for i, line in enumerate(lines):
        if marker in line:  # Si le marqueur est trouvé dans la ligne
            lines[i] = append_str  # Ajouter la chaîne à la fin de la ligne
    
    # Réécrire le fichier avec les modifications
    with open(file_path, 'w') as f:
        f.writelines(lines)

    print(f"Chaîne ajoutée à la fin de la ligne contenant '{marker}' dans {file_path}")



# il va demadner de changer qualque chose
#creer nombre de copies de template 


def copie_template(fjson, template):
    """
    Cette fonction crée des copies du template avec les noms des routeurs.
    
    Attributs : 
        fjson (dict) : Le dictionnaire JSON contenant les informations des routeurs.
        template (str) : Le chemin vers le fichier template à copier.
    """
    for routeur in fjson["reseau"]:
        # Construire le nom de fichier de configuration pour chaque routeur
        num_routeur = routeur["nom"][1:]

        nom_fichier = f"i{num_routeur}_startup-config.cfg"
        
        # Copier le fichier template en utilisant le nom spécifique
        shutil.copy(template, nom_fichier)
    
    print(f"Les fichiers de configuration initiale avec le nom des routeurs ont été créés nom {nom_fichier}.")


# Liste des marqueurs
# marqueurs = ["[Router_name]" ,"[syntaxe_loopback]","[syntaxe_Ge1/0]","[syntaxe_Ge2/0]","[syntaxe_Ge3/0]","[syntaxe_Ge4/0]","[bgp]","[protocole_syntaxe]"]  # Génère une liste de 0 à 9
marqueurs = {
    "router_name": "[router_name]",
    "Loopback0": "[syntaxe_loopback]",
    "GigabitEthernet 1/0": "[syntaxe_Ge1/0]",
    "GigabitEthernet 2/0": "[syntaxe_Ge2/0]",
    "GigabitEthernet 3/0": "[syntaxe_Ge3/0]",
    "GigabitEthernet 4/0": "[syntaxe_Ge4/0]",
    "BGP": "[bgp]",
    "protocole_syntaxe": "[protocole_syntaxe]"
}

def chang_nom_du_routeur(template_R, nom_routeur, marqueurs):
    """
    Fonction qui change le nom du routeur dans le template.
    """
    # Remplace le marqueur correspondant par le nom du routeur
    info = (
        f"hostname {nom_routeur}"
    )
    append_to_configuration_line(template_R, marqueurs.get("router_name"), info)

def generer_interfaces(fjson, template_R, nom_routeur, marqueurs):
    """
    Fonction qui cherche les informations dans le JSON et les met en forme 
    selon le protocole utilisé (OSPF, RIP ou BGP).
    """
    indice_marqueur = 1  # Indice du premier marqueur pour les interfaces

    # Recherche du routeur correspondant dans le JSON
    for routeur in fjson["reseau"]:
        if routeur["nom"] == nom_routeur:
            # Parcourt des interfaces du routeur
            for interface_nom, interface_details in routeur["interfaces"].items():
                # Recherche du protocole associé à cette interface
                protocole_details = interface_details.get("protocole", {})
                protocole_nom = protocole_details.get("nom")

                if protocole_nom == "RIP":
                    # Configuration spécifique à RIP
                    infos = (
                        f" ipv6 address {interface_details['ip']}\n"
                        " ipv6 enable\n"
                        f" ipv6 rip {protocole_details['id']} enable"
                    )
                    append_to_configuration_line(template_R, marqueurs[interface_nom], infos)

                    infos = (
                            "ipv6 router rip 1\n"
                            " redistribute connected\n"
                            "!\n"
                            "ipv6 router rip 2 \n"
                            " redistribute connected"
                        )
                    append_to_configuration_line(template_R, marqueurs["protocole_syntaxe"], infos)


                elif protocole_nom == "OSPF":
                    # Configuration spécifique à OSPF
                    infos = (
                        f" ipv6 address {interface_details['ip']}\n"
                        " ipv6 enable\n"
                        f" ipv6 ospf {protocole_details['routeurOSPF']} area {protocole_details['area']}"
                    )
                    append_to_configuration_line(template_R, marqueurs[interface_nom], infos)
                    infos = (
                        f"ipv6 router ospf {protocole_details['routeurOSPF']}\n" 
                        f" router-id {protocole_details['id']}")
                    append_to_configuration_line(template_R, marqueurs["protocole_syntaxe"], infos)

                else:
                    # Si aucun protocole n'est défini
                    if interface_nom == "Loopback0":
                        infos =( 
                                f" ipv6 address {interface_details['ip']}\n"
                                " ipv6 enable"
                                )
                    else:
                        infos = ("")
                    
                    append_to_configuration_line(template_R, marqueurs["Loopback0"], infos)

            
            # Configuration spécifique à BGP
            bgp_details = routeur["BGP"]
            info =(
                f"router bgp {bgp_details['as']}\n"
                f" bgp router-id {bgp_details['id']}\n"
                " bgp log-neighbor-changes\n"
                " no bgp default ipv4-unicast\n"
                + "\n" .join(f" neighbor {neighbour[0]} remote-as {neighbour[1]}" for neighbour in bgp_details['neighbour']) +"\n"
                + "\n" .join(f" neighbor {neighbour[0]} update-source Loopback0" for neighbour in bgp_details['neighbour'] if bgp_details['as'] == neighbour[1]) +"\n"
                + " !\n"
                " address-family ipv4\n"
                " exit-address-family\n"
                " !\n"
                " address-family ipv6\n"
                + "\n" .join(f"  network {network}" for network in bgp_details["networks"]) +"\n"
                + "\n" .join(f"  neighbor {neighbour[0]} activate" for neighbour in bgp_details['neighbour']) +"\n"
                +" exit-address-family"
            )
            append_to_configuration_line(template_R, marqueurs["BGP"], info)
                # Ajouter la configuration générée dans le template
                
                




fjson = ouvrir_json("reseaux14routeurs.json")



template = "./template2 copy.cfg" #template initiale
copie_template(fjson,template)
for routeur in fjson["reseau"]:
    num_routeur = routeur["nom"][1:]
    print(routeur["nom"])
    template_routeur = nom_fichier = f"i{num_routeur}_startup-config.cfg"
    chang_nom_du_routeur(template_routeur,routeur["nom"],marqueurs)
    generer_interfaces(fjson,template_routeur,routeur["nom"],marqueurs)

    #ajouter parcour qui elimine les marqueurs restant 
    for i in list(marqueurs.values()):
        info = ("")
        append_to_configuration_line2(template_routeur,i,info)


copier_configs_dans_repertoires(repertoires_routeurs, repertoire_sources_config)