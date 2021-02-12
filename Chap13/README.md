# Chapitre 13 : HTML et CSS

## liens utiles
* [une page HTML basique](https://github.com/thfruchart/1nsi-2020/blob/master/Chap13/page_basique.html)
* [w3schools](https://www.w3schools.com/html/default.asp)

# HTML : un langage de balises pour le Web
HTML signifie **HyperText Markup Language** : langage de balises hypertexte
* ce langage permet de décrire avec des **balises** le contenu d'une page web, c'est à dire
   * sa structure (titres, paragraphes, ...)
   * mise en forme (gras, souligné, couleur,...)
   * le contenu du texte 
   * mais aussi, du contenu plus riche : images, ... 
* une **balise** est délimitée par les caractères **`< >`**
   * le nom de la balise s'écrit entre les deux symboles **`< >`**
   * une balise de la forme **`</ >`** est appelée "balise fermante"
   * exemple : balise de paragraphe
      * **`<p>`** est une balise ouvrante, qui marque le début d'un paragraphe.
      * **`</p>`** est la balise fermante correspondante,  qui marque la fin d'un paragraphe.
* le langage HTML permet d'écrire des [liens **hypertexte**](https://fr.wikipedia.org/wiki/Hypertexte) permettant d'accéder directement à d'autres documents (HTML entre autres)

L'objectif du travail dans ce chapitre est de se familiariser avec :
* la stucture d'une page HTML
* les principales balises
* la notion de lien hypertexte
* quelques principes de mise en forme.

# Travail à faire (1) : balises HTML
1. Ecrire une première page HTML, en personnalisant un exemple du site [w3schools](https://www.w3schools.com/html/default.asp)
   * vous pouvez inscrire votre prénom, ou vos initiales
   * mais veillez à ne pas mettre d'autres informations personnelles!
   * une fois le travail effectué :
       * utiliser le bouton 'Save' pour "publier" votre travail
       * m'envoyer par mail un lien vers votre première page html!
2. Ecrire une deuxième page HTML, contenant les éléments suivants : 
   * des titres de différents niveaux
   * plusieurs paragraphes, dont un au moins avec des retour à la ligne
   * des listes imbriquées (numérottées, et non numérottées)
   * un lien hypertexte
   * une image : 
      * libre de droits : par exemple, trouvée sur le site [https://fr.123rf.com/images-libres-de-droits/](https://fr.123rf.com/images-libres-de-droits/)
      * un clic sur l'image doit ouvrir un lien hypertexte vers un article du site Wikipedia en rapport avec l'image
   * aucune mise en forme supplémentaire n'est exigée.
3.  une fois le travail effectué :
    * utiliser le bouton 'Save' pour "publier" votre travail si vous êtes sur  [w3schools](https://www.w3schools.com/html/default.asp)
    * m'envoyer par mail un lien vers votre première page html!
    * si vous travaillez sur votre poste, enregistrez votre fichier et envoyez-le moi en pièce jointe!
    

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

Une description synthétique de CSS est disponible [ici](https://github.com/thfruchart/1nsi-2020/blob/master/Chap13/memento_css3.pdf). 

## Deux balises génériques : `<span>` et `<div>`


