# Formulaire HTML

## 1. Un exemple pour démarrer
#### a. Avec un éditeur de texte:
Créer un fichier `formulaire1.html`, et copier-coller le contenu suivant
```html
<!doctype html>
<html>
 <head>
     <title>
        Un premier formulaire
     </title>
     <meta charset="utf8">
 </head>
 <body>
    <form method="get" action="https://www.qwant.com">
        <p>En quelle langue souhaitez-vous consulter qwant ?</p>
        <input type="radio" name="l" value="fr" id="french" checked><label for="french">Français</label><br>
        <input type="radio" name="l" value="en" id="engl"><label for="engl">Anglais</label><br>
        <input type="radio" name="l" value="de" id="deutsch"><label for="deutsch">Allemand</label><br>
        <input type="radio" name="l" value="es" id="espanol"><label for="espanol">Espagnol</label><br>
        <input type="submit" value="Valider">
    </form>
 </body>
</html>
```

#### b. Ouvrir ce fichier dans un navigateur
#### c. Tester le formulaire
* Sélectionner l'une de langues, cliquer sur le bouton Valider : observer la page qui s'ouvre.
* Puis recommencer l'opération en sélectionnant une autre langue dans le formulaire : quels changements observez-vous ?

#### d. Sauvegarder votre fichier sous le nom `formulaire2.html`
* modifier, toutes la balises `<input type="radio" name="l" ... >` en remplaçant name="l" par name="**q**"
*  tester de nouveau le formulaire : quel changement constatez-vous

#### e. Observer l'URL (dans la barre d'adresse du navigateur)
Essayer d'expliquer comment le choix de l'utilisateur dans le formulaire est "envoyé" au site qwant.com.

## 2. Syntaxe d'un formulaire HTML
#### [Autres exemples de formulaire](https://www.w3schools.com/html/html_forms.asp)
**A retenir** : 
* un formulaire est défini avec une balise html **`<form>  </form>`**
* cette balise peut contenir des éléments de texte "classique" (titre, paragraphe), 
* il existe une balise spécifique aux formulaires :  **`<input>`**
   * l'attribut principal d'une balise <input> est `type`
   * la valeur la plus simple de cet attribut est :  `type="text"` : exemple
      * **`<input type="text" name="nom">`**
      * l'attribut `name` crée un **nom de variable** destinée à recevoir la valeur saisie dans le formulaire.
   * d'autre valeurs sont décrites [dans ce LIEN](https://www.w3schools.com/html/html_form_input_types.asp) voir en particulier : 
      * `<input type="number">`
      *  `<input type="password">`
      *   `<input type="checkbox">`
      *    `<input type="radio">`
   * voir aussi les "menus déroulants" construits avec :   `<select><option>` [ici](https://www.w3schools.com/html/html_form_elements.asp)
* une fois un formulaire rempli, il peut être **envoyé** à l'aide d'un bouton défini par :
   *  `<input type="submit" value="Texte_du_bouton">`
   * la manière dont le formulaire est envoyé est décrite dans la balise   `<form>` avec deux attributs
      *  **`method`** qui peut prendre la valeur **"post"**  ou **"get"** (ou d'autres valeurs que nous n'étudierons pas)
      *  **`action`** qui décrit la ressource qui sera demandée lorsqu'on valide le formulaire. Contrairement à ce que suggère le nom, cet attribut ne décrit pas une action, mais une ressource (un peu comme l'attribut `href` d'une balise `<a>`, ou l'attribut `src` d'une balise `<img>`) 

## 3. get ou post ?
### méthode get
* si un formulaire est envoyé avec la méthode **get**, les noms des paramètres ainsi que leurs valeurs sont envoyées dans l'url.
* la syntaxe de l'url est alors la suivante : 
   * `protocole://nom-ou-adresse/document?n1=v1&n2=v2...&nk=vk` 
      * un **?** sépare la partie décrivant le document de la liste des paramètres
      * chaque paramètre est de la forme **n=v** avec `n` le nom du paramètre et `v` sa valeur
      * les différents paramètres sont séparés par le symbole **&**
#### Quand utiliser la méthode get ?
Comme son nom l'indique, la méthode get est destinée à demander une ressource : 
* cette méthode est appropriée pour un formulaire de recherche, par exemple, et plus généralement, à toute requête qui n'exige pas de mettre à jour certaines données sur le serveur. 
* cette méthode permet de stocker la valeur des paramètres dans l'URL, ce qui est pratique si on souhaite faire un LIEN (à partager, ou à stocker dans ses favoris)
#### Quand NE PAS utiliser la méthode get ?
* Puisque la longueur d'une URL est limitée, avec la méthode get il est impossible d'envoyer un paramètre de taille arbitrairement longue (un message dans un forum par exemple). On n'emploiera donc pas cette méthode si le formulaire contient un champ <textarea> (qui permet de saisir un "long" texte).
* Puisque la valeur des paramètres est affiché dans l'url, **on n'emploiera pas la méthode get pour envoyer des informations personnelles** : adresse mail, ou surtout mot de passe !  
* Si les données envoyées sont destinées à être stockées sur le serveur, l'utilisation de get est impossible. 

## méthode post
* si un formulaire est envoyé avec la méthode **post**, les noms des paramètres ainsi que leurs valeurs sont envoyées dans le corps de la requête.
* la syntaxe de l'url est alors inchangée : 
   * `protocole://nom-ou-adresse/document` 
* le navigateur génère la chaîne des paramètres sous la forme `n1=v1&n2=v2...&nk=vk` mais cette chaîne est envoyée dans le corps de la requête. 



#### Quand utiliser la méthode post ?
Comme son nom l'indique, la méthode post est destinée à envoyer des informations au serveur! 
* dès que les informations envoyées sont destinées à être stockées sur le serveur : la méthode post s'impose.
* dès que les informations envoyées peuvent être "longues" : la méthode post s'impose.
* dès que les informations envoyées sont confidentielles : la méthode post s'impose.
* exemple : 
   * envoyer un message destiné à être publié sur un forum 
   * envoyer un identifiant et un mot de passe

#### Quand ne pas utiliser la méthode post ?
Si on souhaite pouvoir faire un lien vers une page obtenue en envoyant un formulaire, il faut stocker la valeur des paramètres dans l'URL... la méthode post ne convient donc pas. Mais dans tous les autres cas, la méthode post est appropriée. 


# Travail à faire (A)
Ecrire un formulaire qui permet de définir trois variables : `nom` `prenom`  `age`
et qui contient un bouton pour l'envoyer avec la méthode **get** vers la ressource :
* https://www.nsi-premiere.fr/form

# Travail à faire (B)

## 1.  Créer votre formulaire html personnel
Le contenu est libre, mais il devra comporter au moins un exemple de chacun des types suivants : [voir ce LIEN](https://www.w3schools.com/html/html_form_input_types.asp)
 * `<input type="text">`
 * `<input type="number">`
 *  `<input type="password">`
*   `<input type="checkbox">`
*    `<input type="radio">`
## 2. Ajouter un "menu déroulant"
`<select><option>` [voir ce lien](https://www.w3schools.com/html/html_form_elements.asp)

## 3. "envoyer" le formulaire
Comme nous n'avons pas (encore) étudié la programmation côté serveur, vous allez procéder de manière simplifiée : 
* Ajouter l'attribut  **`method="get"`** dans la balise `<form>`
* Ne pas mettre d'attribut `action` (dans ce cas, la cible est la page elle-même) 
* **Créer pour chaque élément de votre formulaire, un attribut `name` définissant le nom de variable** destinée à recevoir la valeur saisie dans le formulaire.
* Tester votre formulaire en observant dans l'URL que les informations renvoyées sont correctes. 
* envoyez-moi par mail le résultat de votre travail.
