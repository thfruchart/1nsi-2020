## EX1
On suppose que le répertoire personnel de l'utilisateur courant est vide. 
* décrire l'effet de chaque  commande ci-dessous, en supposant qu'elles sont effectuées dans l'ordre
* tester en exécutant ces commandes avec  [JSLinux](https://bellard.org/jslinux/vm.html?url=https://bellard.org/jslinux/buildroot-x86.cfg)

1. `cd ~` ouvre le dossier personnel de l'utilisateur
2. `mkdir NSI` crée un nouveau dossier `NSI` 
3. `mkdir NSI/TP`  crée un nouveau dossier `TP` dans le dossier `NSI` 
4. `cd NSI` ouvre le dossier NSI
5. `ls` liste le contenu du dossier NSI (ce dossier contient... le dossier TP)
6. `cd TP` ouvre le dossier TP
7. `cd ..` ouvre le dossier parent, c'est à dire NSI
8. `ls` liste le contenu du dossier NSI (ce dossier contient... le dossier TP)
9. `touch fic1` crée un nouveau fichier nommé `fic1` (dans le dossier NSI)
10. `touch TP/fic2`   crée un nouveau fichier nommé `fic2` (dans le dossier NSI/TP)
12. `ls` liste le contenu du dossier courant (NSI) : ce dossier contient  le dossier **TP** et le fichier **fic1**
13. `ls TP` liste le contenu du dossier TP : ce dossier contient le fichier **fic2**
14. `mv fic1 TP` déplace le fichier **fic1** vers le dossier **TP**
15. `ls` liste le contenu du dossier courant (NSI) : ce dossier contient  le dossier **TP** (mais pas le fichier fic1 vient d'être déplacé)
16. cd TP
17. ls
18. cp fic2 ..
19. ls
20. cd ..
21. ls
