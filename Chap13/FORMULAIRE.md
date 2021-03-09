# Que se passe-t-il lorsqu'un navigateur "ouvre" une page web ? 
* cette page est définie par une **adresse** appelée **URL** (*Uniform Resource Locator*).
* une URL se présente (sous forme simplifiée) sous la forme `protocole://nom-ou-adresse/document`
   *  par exemple, l'URL de cette page est https://github.com/thfruchart/1nsi-2020/new/master/Chap13/FORMULAIRE.md 
   *  cette URL se décompose en  :
      * `https` qui est le nom du protocole : c'est l'ensemble des règles qui définissent la manière dont les informations sont échangées
      *   `github.com` : c'est le nom du domaine du serveur 
      *   `thfruchart/1nsi-2020/new/master/Chap13/FORMULAIRE.md ` correspond à l'adresse du "document" qui est demandé par le navigateur
* lorsqu'on tape cette adresse dans la barre d'adresse d'un navigateur : 
   1. le navigateur isole le nom de domaine :   `github.com`  
   2. le navigateur effectue une **requête DNS** pour obtenir l'adresse IP du serveur Web qui héberge le site
   3. le navigateur se connecte au serveur et effectue une requête HHTP : [voir ce lien](https://pixees.fr/informatiquelycee/n_site/nsi_prem_http.html)

# Formulaire HTML

