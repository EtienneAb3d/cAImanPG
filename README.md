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

Wait for the responses, it should be like:

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
> En ce qui concerne la nourriture pour votre chat, je suis désolé, mais je ne suis pas en mesure de vous aider car je suis spécialisé dans le support technique pour les ordinateurs. Je vous suggère de contacter un vétérinaire ou une animalerie pour obtenir des conseils.
> 
> J'espère que ces informations vous seront utiles. N'hésitez pas à me contacter si vous avez d'autres questions techniques.

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
