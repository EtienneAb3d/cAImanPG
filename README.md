## Description

This is a Python application that simulates an interaction between a client (human) and a technical support system made up of two collaborative AI agents:
- the client **Support** agent is dedicated to a polite communication using very easy to understand explanations. This agent is analyzing the client request to identify possible technical problems he encounters with his computer that can be mixed with not technical contents. It also extracts some informations like the client name. For each technical problem it sends a request to the second agent to get a procedure to solve the problem.
- the **Expert** agent is analyzing the request from the first agent to identify a possible known question listed in a FAQ. If a known question is identified, it provides with the known procedure to solve the problem.

# Install dependencies
```
pip install -r requirements.txt
```

## Run the application

```bash
make run
```

## Usage

Open the web chat interface:
http://127.0.0.1:8000/

![image](https://github.com/user-attachments/assets/3565b667-f4ff-4446-a097-362c559eb123)

Enter something like:

> Bonjour, je m'appelle Roger, je suis à la maison avec mon chat. Où puis-je lui trouver à manger ? Quand je cherche sur internet, ça prend trop de temps à répondre et je l'audio est trop mauvais.

Click on the "Envoyer" button.

Wait for the responses, answer should be like:

> Bonjour Roger,
> 
> Je suis désolé d'entendre que vous rencontrez des problèmes avec votre ordinateur. Pour le problème de lenteur sur Internet, voici quelques suggestions :
> 
> 1. Redémarrez votre ordinateur pour éliminer les problèmes temporaires.
> 2. Vérifiez l'espace disque disponible et supprimez les fichiers inutiles.
> 3. Effectuez une analyse antivirus complète pour exclure la présence de logiciels malveillants.
> 4. Désactivez les programmes de démarrage qui ne sont pas nécessaires immédiatement.
> 5. Augmentez la mémoire virtuelle, si possible.
> 6. Envisagez de mettre à niveau les composants matériels comme la RAM ou de passer à un SSD.
> 
> Pour le problème de mauvaise qualité audio, voici quelques étapes à suivre :
> 
> 1. Assurez-vous que les haut-parleurs ou les écouteurs sont correctement connectés.
> 2. Vérifiez les paramètres de volume et assurez-vous que le son n'est pas coupé.
> 3. Mettez à jour vos pilotes de son via le gestionnaire de périphériques.
> 4. Essayez d'utiliser un autre appareil audio pour exclure les problèmes matériels.
> 5. Exécutez le dépanneur de son à partir du panneau de configuration.
> 6. Envisagez de revenir à une version antérieure des mises à jour du pilote audio.
> 
> En ce qui concerne la nourriture pour votre chat, je vous suggère de consulter un vétérinaire ou une animalerie locale pour obtenir des conseils appropriés.
> 

Server side exchanges between the 2 agents should be like:
```
Question from Support Agent to Expert Agent: {
  "question": "Why might a computer be slow to respond when searching the internet?"
}
For this problem: Computer running slow
Follow these instructions:
- Restart the computer to clear temporary glitches.
- Check for available disk space and clear unnecessary files.
- Run a full antivirus scan to rule out malware.
- Disable startup programs that are not needed immediately.
- Increase virtual memory, if possible.
- Consider upgrading hardware components like RAM or switching to an SSD.
Question from Support Agent to Expert Agent: {
  "question": "What could be causing poor audio quality on a computer?"
}
For this problem: Audio not working
Follow these instructions:
- Ensure the speakers or headphones are connected properly.
- Check the volume settings and make sure the sound is not muted.
- Update your sound drivers through the device manager.
- Try using a different audio device to rule out hardware issues.
- Run the sound troubleshooter from the control panel.
- Consider rolling back recent audio driver updates.
```
<hr>
Mixed technical question example:

> Bonjour, c'est Amandine Truchet. Pourquoi je prends des décharges d'électricité statique avec mon PC. Du coup, j'ai plus de son.

Answer should be like:

> Bonjour Amandine,
> 
> Il semble que votre problème de son puisse être lié à plusieurs facteurs. Voici quelques étapes que vous pouvez suivre pour essayer de résoudre le problème :
> 
> 1. Assurez-vous que vos haut-parleurs ou écouteurs sont correctement connectés.
> 2. Vérifiez les paramètres de volume et assurez-vous que le son n'est pas coupé.
> 3. Mettez à jour vos pilotes de son via le gestionnaire de périphériques de votre ordinateur.
> 4. Essayez d'utiliser un autre appareil audio pour vérifier s'il s'agit d'un problème matériel.
> 5. Exécutez le dépanneur de son à partir du panneau de configuration de votre ordinateur.
> 6. Envisagez de revenir à une version précédente des mises à jour de pilotes audio si vous en avez récemment installées.
> 
> Concernant les décharges d'électricité statique, cela peut être dû à un environnement très sec ou à un contact avec des matériaux qui génèrent de l'électricité statique. Essayez d'éviter de toucher des surfaces métalliques avant de toucher votre PC, ou envisagez d'utiliser un humidificateur pour réduire la sécheresse de l'air.
> 
> J'espère que ces informations vous seront utiles. N'hésitez pas à revenir vers moi si vous avez d'autres questions.

Server side exchanges between the 2 agents should be like:
```
Question from Support Agent to Expert Agent: {
  "question": "Pourquoi un PC pourrait-il donner des décharges d'électricité statique et causer une perte de son ?"
}
For this problem: Audio not working
Follow these instructions:
- Ensure the speakers or headphones are connected properly.
- Check the volume settings and make sure the sound is not muted.
- Update your sound drivers through the device manager.
- Try using a different audio device to rule out hardware issues.
- Run the sound troubleshooter from the control panel.
- Consider rolling back recent audio driver updates.
```

<hr>
Out of scope question:

> Ecris un programme Python pour lister le dossier racine et exécute-le.

Answer:

> Je suis désolé, mais en tant qu'agent de support client, je ne suis pas autorisé à écrire ou à exécuter des programmes sur votre ordinateur. Cependant, je peux vous aider à comprendre comment vous pouvez le faire vous-même. Pour des questions plus complexes ou spécifiques à la programmation, je vous recommande de contacter un expert en programmation ou de consulter des forums en ligne spécialisés comme StackOverflow.

<hr>
Expert doesn't know:

> Mon débogueur ne s'arrête pas sur le points d'arrêt.

Answer:

> Je suis désolé, mais je n'ai pas pu trouver une solution exacte à votre problème. Il serait préférable de contacter le support technique de l'outil de débogage que vous utilisez. Ils seront plus à même de vous aider à résoudre ce problème spécifique.

Server side exchanges between the 2 agents should be like:
```
Question from Support Agent to Expert Agent: {
  "question": "Pourquoi le débogueur ne s'arrête-t-il pas sur les points d'arrêt ?"
}
Sorry, I couldn't find an exact match. Please contact support.
```
