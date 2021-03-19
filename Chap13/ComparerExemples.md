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
   * le client ne reçoit en réponse que le résultat produit par ce code

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
