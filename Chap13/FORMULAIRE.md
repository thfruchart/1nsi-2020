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
   * la valeur la plus simple de cet attribut est :  `type="text"`
   * d'autre valeurs sont décrites [ici](https://www.w3schools.com/html/html_form_elements.asp)
* une fois un formulaire rempli, il peut être **envoyé** à l'aide d'un bouton défini par :
*  `<input type="submit" value="Texte_du_bouton">`
   * la manière dont le formulaire est envoyé est décrite dans la balise   `<form>` avec deux attributs
      *  **`method`** qui peut prendre la valeur **"post"**  ou **"get"** (ou d'autres valeurs que nous n'étudierons pas)
      *  **`action`** qui décrit la ressource qui sera demandée lorsqu'on valide le formulaire. Contrairement à ce que suggère le nom, cet attribut ne décrit pas une action, mais une ressource (un peu comme l'attribut `href` d'une balise `<a>`, ou l'attribut `src` d'une balise `<img>`) 
