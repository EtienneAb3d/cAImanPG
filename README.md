## Description

This is a Python application that simulates an interaction between a client (human) and a technical support system made up of two collaborative AI agents:
- the client **Support** agent is dedicated to a polite communication using very easy to understand explanations. This agent is analyzing the client request to identify possible technical problems he encounters with his computer ignoring all not technical contents. It also extracts some informations like the client name. For each technical problem it sends a request to the second agent to get a procedure to solve the problem.
- the **Expert** agent is analyzing the request from the first agent to identify a possible known question listed in a FAQ. If a known question is identified, it provides with the known procedure to solve the problem.

# Installation
```
pip install -r requirements.txt
```

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
```
{
  "question": "Bonjour, je m'appelle Roger, je suis à la maison avec mon chat. Où puis-je lui trouver à manger ? Quand je cherche sur internet, ça prend trop de temps à répondre et je l'audio est trop mauvais."
}
```
- click on "Execute"
- wait for the "Responses", it should be like:
```
200	
Response body

Bonjour Roger, 

Je suis désolé d'apprendre que vous rencontrez des problèmes avec votre ordinateur. Voici quelques suggestions pour résoudre les problèmes que vous avez mentionnés.

Pour le problème de lenteur de votre ordinateur lors de la recherche sur Internet, vous pouvez essayer les étapes suivantes :
1. Redémarrez votre ordinateur pour éliminer les problèmes temporaires.
2. Vérifiez l'espace disque disponible et supprimez les fichiers inutiles.
3. Effectuez une analyse antivirus complète pour exclure la présence de logiciels malveillants.
4. Désactivez les programmes de démarrage qui ne sont pas nécessaires immédiatement.
5. Augmentez la mémoire virtuelle, si possible.
6. Envisagez de mettre à niveau les composants matériels comme la RAM ou de passer à un SSD.

En ce qui concerne le problème de la mauvaise qualité audio, voici quelques étapes que vous pouvez essayer :
1. Assurez-vous que les haut-parleurs ou les écouteurs sont correctement connectés.
2. Vérifiez les paramètres de volume et assurez-vous que le son n'est pas coupé.
3. Mettez à jour vos pilotes de son via le gestionnaire de périphériques.
4. Essayez d'utiliser un autre appareil audio pour exclure les problèmes matériels.
5. Exécutez le dépanneur de son à partir du panneau de configuration.
6. Envisagez de revenir à une version précédente des mises à jour du pilote audio.

J'espère que ces suggestions vous aideront à résoudre vos problèmes. Si vous avez besoin d'aide supplémentaire, n'hésitez pas à me le faire savoir.
```
