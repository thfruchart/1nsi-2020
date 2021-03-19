# Exemple 1
```html
<!doctype html>
<html>
  <head>
    <title>
     Exemple 1
    </title>
    <meta charset="utf-8"/>
  </head>
  <body>
    <form action="php-calcul.php" method="post">
      <input type="text" name="n1"/><div>+</div>
      <input type="text" name="n2"/>
      <input type="submit" value="CALCULER"/>
    </form>
  </body>
</html>
```

Ce fichier contient  : 
* un formulaire permettant de saisir deux valeurs n1  et  n2
* la méthode **post** de ce formulaire permet d'envoyer une requête vers la page `php-calcul.php` avec :
   * le paramètre n1 entré dans le premier champ du formulaire
   * le paramètre n2 entré dans le premier champ du formulaire

## Côté CLIENT
un client qui a saisi les valeurs 12 et 25 dans le formulaire, recevra du serveur la réponse suivante : 
```html
<!doctype html>
<html>
 <head>
     <title>
        Résultat du calcul
     </title>
     <meta charset="utf8">
 </head>
 <body>
<p>
    12 + 25 = 37</p>
 </body>
</html>
```

Pour produire cette page html, le serveur a exécuté les instructions contenues dans le fichier  `php-calcul.php`.
## Côté serveur
* on donne le contenu du fichier  `php-calcul.php` qui est exécuté sur le serveur 
* Attention : 
   * le client n'a PAS accès au code php qui est exécuté.
   * le client ne "connaît" que le résultat produit par ce code, qui est envoyé comme réponse à sa requête.

```php
<!doctype html>
<html>
 <head>
     <title>
        Résultat du calcul
     </title>
     <meta charset="utf8">
 </head>
 <body>
<p>
    <?php
    if (isset($_POST['n1']) && isset($_POST['n2']) )
    {
        $n1 = $_POST['n1'];
        $n2 = $_POST['n2'];
        $s = $n1 + $n2;
        echo "$n1 + $n2 = $s";

    }
    else { echo "Erreur";}
    ?>
</p>
 </body>
</html>
```
* ce fichier php contient des balises html "classique"
*  il contient également deux  balises spéciales "php" : 
   *  balise ouvrante  `<?php`
   *  balise fermante `?>`
   *  le **code php** contenu entre ces deux balises est **exécuté sur le serveur**
   *  le résultat produit (ici le contenu d'un paragraphe) est envoyé au client avec l'ensemble du fichier.

### Conclusion
Dans cet exemple1, 
* les valeurs entrées dans le formulaires sont envoyées au serveur
* l'addition des deux valeurs saisies par le client est exécutée **sur le serveur**
* la réponse est envoyée du serveur au client, qui peut alors l'afficher.

# Exemple 2
Dans cet exemple2, le client dispose du code html suivant : 
```html
<!doctype html>
<html>
  <head>
    <title>
      Exemple2
    </title>
    <meta charset="utf-8"/>
  <script>
  function maFonction() {
   var nombre1 = document.getElementById("n1").value;
   var nombre2 = document.getElementById("n2").value;
   var resultat = Number(nombre1) + Number(nombre2);
   var texte = nombre1 + " + " + nombre2 + ' = ' + resultat;
   document.getElementById("resu").innerText = texte;
  }
  </script>
  </head>
  <body>
    <form>
      <input type="text" id="n1"/><div>+</div>
      <input type="text" id="n2"/>
      <input type="button" onclick="maFonction()" value="CALCULER"/>
    </form>
    <p id="resu"></p>
  </body>
</html>
```
#### On remarque que : 
* l'apparence est la même que dans l'exemple1
* mais la balise `<form>` n'a pas d'attibut method, ni action
* le bouton affiché n'est pas de type `submit` mais simplement `button`
* lorsque l'utilisateur saisit des valeurs, puis clique sur le bouton, **le formulaire n'est pas envoyé** ! 

#### Comment le résultat est-il affiché ?
* le bouton dispose d'un attribut `onclick`
* cet attribut permet d'exécuter `MaFonction()` lorsque le bouton est cliqué.
* cette fonction est définie dans la balise `<script>` située dans l'entête du fichier. 
* la fonction, écrite en Javascript, effectue le calcul et affiche la réponse dans le paragraphe dont l'id est `resu`. 

Lorsque le bouton est cliqué :
* **c'est le navigateur du client qui effectue le calcul** et affiche la réponse, grâce au code Javascript contenu dans le fichier. 
* Une fois la page chargée, l'utilisateur peut effectuer autant de calculs qu'il souhaite, sans avoir besoin de se connecter au serveur.

# Comparaison
* dans l'exemple1, l'addition est effectuée côté **serveur** à l'aide d'instructions écrites en **php**. 
* dans l'exemple2, l'addition est effectuée côté **client** à l'aide des instructions écrites en **javascript** dans le fichier `ex2.html`
* on peut visualiser la différence entre ces deux langages en saisissant une valeur numérique dans le premier champ du formulaire, et un texte dans le deuxième champ. Ce cas est géré différemment par javascript et php!
