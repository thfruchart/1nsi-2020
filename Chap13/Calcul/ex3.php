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
    }
	else{
		$n1 = 0;
        $n2 = 0;
        $s = 0;
	}
    ?>
	<form  method="post">
			  <input type="text" name="n1" value="<?=$n1?>"/><div>+</div>
			  <input type="text" name="n2"  value="<?=$n2?>"/>
			  <input type="submit" value="CALCULER"/>
		 </form>
	<?= "$n1 + $n2 = $s";?>
</p>
 </body>
</html>
