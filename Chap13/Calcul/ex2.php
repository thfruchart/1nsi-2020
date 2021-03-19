<!doctype html>
<html>
	<head>
		<title>
			Addition
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