## Description

Python application that simulates an interaction between a user and a technical support system made up of two collaborative AI agents. 

# Installation
'''
pip install -r requirements.txt
'''

## Run the application

```bash
make run
```

## Usage

Swagger docs are available at http://127.0.0.1:8000/docs#/

## Test
http://127.0.0.1:8000/docs#/default/chat_chat_post

- open "Chat" section
- click on "Try it out"
- enter something like: 
'''
{
  "question": "Bonjour, je m'appelle Roger, je suis à la maison avec mon chat. Où puis-je lui trouver à manger ? Quand je cherche sur internet, ça prend trop de temps à répondre."
}
'''
- click on "Execute"
- wait for the "Responses", it should be like:
'''
200	
Response body

Bonjour Roger, 

Je suis désolé d'apprendre que votre ordinateur est lent lors de vos recherches sur Internet. Cela peut être dû à plusieurs facteurs. Voici quelques étapes que vous pouvez suivre pour améliorer la vitesse de votre ordinateur :

1. Redémarrez votre ordinateur : cela peut aider à éliminer les problèmes temporaires.
2. Vérifiez l'espace disque disponible : si votre disque est presque plein, cela peut ralentir votre ordinateur. Essayez de supprimer les fichiers inutiles.
3. Faites une analyse antivirus complète : un logiciel malveillant peut ralentir votre ordinateur.
4. Désactivez les programmes de démarrage qui ne sont pas nécessaires immédiatement.
5. Augmentez la mémoire virtuelle, si possible.
6. Envisagez de mettre à niveau les composants matériels comme la RAM ou de passer à un SSD.

J'espère que ces conseils vous aideront à améliorer la vitesse de votre ordinateur. Si vous avez besoin d'aide supplémentaire, n'hésitez pas à me le faire savoir.
'''
