# CSS : une question de style
## Balise, attribut, valeur
En HTML, chaque **balise** peut contenir un ou plusieurs **attributs** qui reçoivent chacun une **valeur**.

Un exemple déjà rencontré est celui de la balise **`<a>`** qui contient un attribut **`href`** dont la valeur est un lien hypertexte : 
* exemple 
   * `<a href="https://github.com/thfruchart/1nsi-2020/edit/master/Chap13/README.md">Lien vers cette page</a>` 
* résultat affiché :
   * [Lien vers cette page](https://github.com/thfruchart/1nsi-2020/edit/master/Chap13/README.md)

## L'attribut style
Chaque balise peut recevoir un attribut style. 
Les valeurs décrites pour cet attribut ne s'appliquent qu'à la partie du document commandée par cette balise (entre la balise ouvrante et la balise fermante). 

Les valeurs possibles pour un attribut style sont très nombreuses : elles sont écrites en langage CSS.

CSS signifie "Cascading Style Sheets" soit *feuilles de style en cascade*. Ce nom vient de ce qu'on peut écrire des règles CSS qui s'appliquent "en cascade" aux divers éléments contenus dans des balises HTML. 

Une idée de la richesse de CSS est accessible [dans ce memento](https://github.com/thfruchart/1nsi-2020/blob/master/Chap13/memento_css3.pdf). 

* exemple : 
   * `<p style="background-color: orange;">Paragraphe à fond orange</p>`
* syntaxe :
   * la valeur de l'attribut `style` est écrite entre `"` après le signe `=`
   * cette valeur se décompose en : 
      * `background-color` qui est le nom d'une propriété CSS
      * `:`
      * `orange` qui est la valeur de la propriété 
      * `;`  permet d'écrire plusieurs propriétés à la suite
   
   
## Deux balises génériques : `<span>` et `<div>`
Pour permettre de délimiter librement une partie de document qui ne correspondrait pas à une simple balise, HTML utilise deux balises "génériques":
* `<span>` dont l'affichage est "inline". 
   * Les éléments "inline" sont juxtaposés horizontalement tant que de la place est disponible ; ensuite l'affichage reprend dans la ligne du dessous.
* `<div>` dont l'affichage est "bloc".
   * Chaque élément "block" occupe toute la largeur disponible. 
   * Plusieurs élément "block" successifs sont affichés les uns en dessous des autres. 

## Deux attibuts spécifiques pour identifier les élements d'un document HTML
Chaque balise peut également recevoir deux attibuts particuliers
* `id` : identifiant unique dans tout le document, qui permet de spécifier une balise en particulier.
* `class` : nom de classe, qui peut être commun à plusieurs balises différentes dans un même document. 
   * une même balise peut recevoir plusieurs noms de classes séparés par des espaces. 
   * `class="nom1 nom2 nom3"`

## Règles CSS
* Il est possible d'utiliser l'attribut style d'une balise pour définir le style qu'on souhaite lui appliquer.
* Il est également possible d'écrire une liste de **règles CSS**  dans l'entête d'un document (entre `<head>` et `</head>`) : ces règles s'appliqueront à tout un document.
   *  ces règles sont à écrire entre les balises 
      * `<style>` et
      * `</style>`
 
* Enfin, on peut stocker des règles dans un fichier CSS, de sorte que ces règles s'appliqueront à toutes les pages HTML d'un site. 
   * dans ce cas, on écrit dans l'entête :
      * `<link type="text/css" rel="stylesheet"  href="style.css" />`

### Structure d'une règle CSS
On peut écrire une règle CSS avec la syntaxe : 

```
nom_de_balise { propriété1 : valeur1;
                ...
                propriéték : valeurk
}
```

ou 
```
#nom_id { propriété1 : valeur1;
          ...
          propriéték : valeurk
}
```
ou 
```
.nom_de_classe { propriété1 : valeur1;
                 ...
                 propriéték : valeurk
}
```
ou 
```
* { propriété1 : valeur1;
                 ...
                 propriéték : valeurk
}
```
Le sélecteur peut donc être : 
* un nom de balise, 
   * dans ce cas, les propriétés décrites s'appliquent à toutes les balises qui portent ce nom
* un nom d'id 
   * dans ce cas, les propriétés décrites s'appliquent à l'unique balise qui possède cet id
* ou un nom de classe 
   * dans ce cas, les propriétés décrites s'appliquent à toutes les balises qui appartiennent à cette classe.
* ou `*`
   * dans ce cas, la propriété s'applique à n'importe quelle balise. 
   
#### On peut appliquer une même règle à plusieurs sélecteurs, séparés par des virgules : 
```
h1, h2, h3 {propriété : valeur;
}
```
Dans ce cas tous les titres de niveau 1, 2 ou 3 appliquent la propriété.

#### IL est églement possible d'enchaîner les selecteurs :
```
.classe3  p  { propriété : valeur;
}
```
Dans ce cas, la propriété ne s'applique qu'aux balises `<p>`  contenues dans une balise appartenant à la classe3 !

# Travail à faire (2)
* Mettre en forme le contenu du fichier [exercice.html ](https://github.com/thfruchart/1nsi-2020/blob/master/Chap13/exercice.html)
* les consignes de mise en forme sont contenues dans le fichier!
   * on pourra commencer par définir un attribut style pour les balises
   *  écrire ensuite toutes les règles css utiles dans l'entête du fichier.
