# Systèmes d'exploitation

## lien vers cours en ligne
## lien vers TP en ligne

## commandes à exécuter dans [JSLinux](https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192)
### en tant que root : définir groupe et utilisateurs
* `addgroup eleve`
* `adduser -G eleve max`
* `adduser -G eleve elsa`
* `adduser toto`

### en tant que **max**
* `su max`
* `whoami`
* `cd`
* `pwd`
* `ls`
* `mkdir documents`
* `ls`
* `cd documents/`
* `touch fichier.max`
* `ls -l`
* `chmod o-r fichier.max`
* `ls -l`
* `nano fichier.max`
* avec l'éditeur nano : 
   * écrire une ligne dans le fichier, par exemple : `Ecriture d'une ligne par Max !`
   * sauvegarder avec Ctrl+S
   * quitter nano avec Ctrl+Q
 * `cat fichier.max`

### en tant que **elsa**
* `su elsa`
* `whoami`
* `ls -l`
* `cat fichier.max`
* `nano fichier.max`

### en tant que **toto**
* `su toto`
* `ls -l`
* `cat fichier.max`



