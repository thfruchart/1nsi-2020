# Architecture Client-Serveur
Dans l’architecture Client-Serveur, on trouve en général un serveur et plusieurs clients. 
Le serveur est une machine qui traite les requêtes du client et lui envoie éventuellement une réponse.

Il y a donc deux types d’application installés sur les machines :
* l’application « serveur » : écoute en attendant des connexions des clients ;
* les applications « client » : se connectent au serveur.

![image](https://user-images.githubusercontent.com/66477650/110476443-4562d000-80e2-11eb-81c1-3201a93cfa41.png)

## Etapes d'une communication Client-Serveur
![image](https://user-images.githubusercontent.com/66477650/110476488-51e72880-80e2-11eb-9733-8872ed9d9d71.png)
#### Le serveur :
1. attend une connexion de la part du client ;
2. accepte la connexion quand le client se connecte ;
3. échange des informations avec le client ;
4. ferme la connexion.

#### Le client :
1. se connecte au serveur ;
2. échange des informations avec le serveur ;
3. ferme la connexion.



# Que se passe-t-il lorsqu'un navigateur "ouvre" une page web ? 
Le navigateur est le programme **client**, et la page web demandée est hébergée sur un ordinateur où s'exécute en permanence un programme **serveur**.

* Chaque page Web est définie par une **adresse** appelée **URL** (*Uniform Resource Locator*).
* une URL peut se présenter sous la forme (simple) `protocole://nom-ou-adresse/document`
   *  par exemple, l'URL de cette page est https://github.com/thfruchart/1nsi-2020/new/master/Chap13/Requete.md 
   *  cette URL se décompose en  :
      * `https` qui est le nom du protocole : c'est l'ensemble des règles qui définissent la manière dont les informations sont échangées
      *   `github.com` : c'est le **nom du domaine** du serveur 
      *   `thfruchart/1nsi-2020/new/master/Chap13/Requete.md ` décrit la localisation du "document" (ou *ressource*) qui est demandé par le navigateur
* lorsqu'on tape cette adresse dans la barre d'adresse d'un navigateur : 
   1. le navigateur isole le nom de domaine :   `github.com`  
   2. le navigateur effectue une **requête DNS** pour obtenir l'adresse IP du serveur Web qui héberge le site
   3. le navigateur établit une connexion avec le serveur avec les protocoles TCP/IP
   4. une fois la connexion établie, le navigateur effectue une **requête HTTPS, ou HTTP** : [voir ce lien](https://pixees.fr/informatiquelycee/n_site/nsi_prem_http.html)
   5. lorsqu'il reçoit la réponse du serveur, il peut traiter cette réponse (effectuer d'autres requêtes) puis afficher la page.


## requête "simple" ou requête "avec paramètres"
* dans les cas les plus simples, la requête envoyée par le client se limite à demander une ressource hébergée sur le serveur : cette requête est traitée directement.
* dans d'autre cas, le client envoie avec sa requête des **paramètres** qui sont traités par le serveur
   * cela signifie qu'avant d'envoyer la ressource demandée, le serveur exécute un programme (écrit en PHP, en Python ou autre)
   * ce programme produit du contenu (html en général) qui est renvoyé en réponse au client.
   * un exemple courant de ce type de requête est celui d'un **moteur de recherche** :
      *  tous les clients qui se connectent à un même serveur ne cherchent pas la même chose
      *  avant d'envoyer sa réponse, le serveur doit exécuter un programme qui "traite" la demande du client

La suite du cours présente la manière la plus classique d'adresser une requête avec paramètres : l'utilisation d'un formulaire.
