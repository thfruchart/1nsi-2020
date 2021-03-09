# Formulaire HTML

## 1. Un exemple pour démarrer
Avec un éditeur de texte, créer un fichier formulaire1.html, et copier-coller le contenu suivant
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

