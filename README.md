# Gns_project
Notre code python se base un fichier json pour génèrer un fichier config pour chaque routeur, et le copie dans le fichier de configuration du routeur correspondant.
Pour générer les fichiers config, le code parcourt un template avec des marqueurs a des endroits précis, et les remplace par les bonnes configs en fonction des données du routeur décrit par le fichier json.
Comment utiliser le code : Il faut deja un projet gns en cours avec les 14 routeurs et leur liens physiques, notre code ne génère que les configs. Il faut ensuite, repérer le chemin vers les fichiers config de chaque routeur, et les mettre dans le code python pour qu'il puisse copier les nouveaux fichiers config qu'il a généré aux bons endroits. Il suffit ensuite de renseigner le chemin vers le repertoire contenant les fichiers configs générés, et le code s'occupera du reste! 
Une fois le code éxécuté, le reseau présent est donc un réseau composé de 14 routeurs, séparé en 2 AS contenat chacun 7 routeurs : l'AS 111 et 112. Le premier route en RIP et l'autre en OSPF avec leur interfaces physiques. Les 2 sont liés avec une config BGP, et chaque AS est configurée en full-mesh iBGP, avec des loopbacks (interfaces virtuelles). Par contre, les routeurs des bordures d'AS sont liés en eBGP avec leurs interfaces physiques. 
Avec cette configuration, tous les routeurs sont atteignables d'Est en Ouest. 
