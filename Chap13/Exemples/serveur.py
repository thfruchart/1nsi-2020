# serveur.py

from socket import socket, AF_INET, SOCK_STREAM

reponse = b"""HTTP/1.1  OK
host : mon site avec python
Content-Type : text /html\n
<!doctype html>
<html>
 <head>
     <title>
        Page de mon serveur python
     </title>
     <meta charset="utf8">
 </head>
 <body>
    <h1>Bonjour</h1>
    <h2>voici l'unique page de mon serveur Python !</h2>
 </body>
</html>"""

s = socket(AF_INET, SOCK_STREAM)
s.bind(("",12345))

s.listen(5)
while True:
    connexion, adresse = s.accept()
    print("connexion de", adresse)
    req = connexion.recv(1024).decode()
    if req != "":
        print(req)
        print()
        connexion.send(reponse)
    connexion.close()

print("Fin")
s.close()
