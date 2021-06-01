<?php
    if (isset($_GET['q1'])) {$q1 = $_GET['q1'];} else {$q1 = '';}
	if (isset($_GET['q2'])) {$q2 = $_GET['q2'];} else {$q2 = '';}
	if (isset($_GET['q3'])) {$q3 = $_GET['q3'];} else {$q3 = '';}
	if ($q1!='' && $q2!='' && $q3!='')
    {  // le calcul du score est possible
		$score = 0;
        if ($q1=='B') {$score= $score+1;};
		if ($q2=='A') {$score= $score+1;};
		if ($q3=='C') {$score= $score+1;};
    }
	elseif ($q1!='' || $q2!='' || $q3!='') // il manque certaines réponses
	{$score = 'merci de répondre à toutes les questions !';}
	 else {$score='';}
?>
<!doctype html>
<html lang="fr">
 <head>
     <title>
        Questionnaire moins facile
     </title>
     <meta charset="utf8">
 </head>
 <body>
 
	<form name="questionnaire" id="questionnaire" method="get">
	<h2> Quelle est la réponse correcte à la question 1 ?</h2>
	<p><input type="radio" name="q1" value="A">A
		  <input type="radio" name="q1" value="B">B 
		  <input type="radio" name="q1" value="C">C
		  <input type="radio" name="q1" value="D">D
	 </p>

	<h2> Quelle est la réponse correcte à la question 2 ?</h2>
	<p>
	<input type="radio" name="q2" value="A">A
	<input type="radio" name="q2" value="B">B
	<input type="radio" name="q2" value="C">C
	<input type="radio" name="q2" value="D">D</p>

	<h2> Quelle est la réponse correcte à la question 3 ?</h2>
	<p>
	<input type="radio" name="q3" value="A">A
	<input type="radio" name="q3" value="B">B
	<input type="radio" name="q3" value="C">C
	<input type="radio" name="q3" value="D">D</p>

	<input type="submit" value="Calculer le score">
	</form>

	<p> Votre score : <span id="resultat"> <?= $score ?> </span></p>
 </body>
</html>






