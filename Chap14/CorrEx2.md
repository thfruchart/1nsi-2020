# Corrigé
## Ex2
On suppose que le répertoire personnel de l'utilisateur courant est vide. 
* décrire l'effet de chaque  commande ci-dessous, en supposant qu'elles sont effectuées dans l'ordre
* tester en exécutant ces commandes avec  [JSLinux](https://bellard.org/jslinux/vm.html?url=https://bellard.org/jslinux/buildroot-x86.cfg)

1. `cd` : change le dossier courant => dossier par défaut de l'utilisateur
2. `mkdir TEST` crée un dossier nommé TEST dans le dossier courant
3. `cd TEST`  : change le dossier courant => TEST
4. `touch fichier`: crée un nouveau fichier dans le dosser courant
5. `touch ../fic`: crée un nouveau fichier dans le dossier parent
6. `ls -l`  : liste longue des fichiers du répertoire courant
7. `chmod o+w fichier` : ajoute les droits en écriture (w) pour les autres utilisateurs (o) de fichier
8. `ls -l` : liste longue des fichiers du répertoire courant (on peut vérifier que les autres utilisateurs ont bien les droits en écriture sur fichier)
9. `chmod a-w fichier` : supprime les droits en écriture pour TOUS les utilisateurs (a)
10. `ls -l` : liste longue des fichiers du répertoire courant (on peut vérifier que tous les utilisateurs n'ont PAS les droits en écriture sur fichier)
