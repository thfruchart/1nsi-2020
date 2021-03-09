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
* Sélectionner l'une de langues, puis cliquer sur le bouton Valider
*  Comparer ce qu'on obtient en sélectionnant une autre langue

#### d. Sauvegarder votre fichier sous le nom `formulaire2.html`
* modifier, toutes la balises `<input type="radio" name="l" ... >` en remplaçant name="l" par name="**q**"
*  tester de nouveau le formulaire : quel changement constatez-vous

#### e. Observer l'URL (dans la barre d'adresse du navigateur)
Essayer d'expliquer comment le choix de l'utilisateur dans le formulaire est "envoyé" au site qwant.com.
