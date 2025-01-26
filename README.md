## Description

This is a Python application that simulates an interaction between a client (human) and a technical support system made up of multiple collaborative AI agents:
- the client **Support** agent is dedicated to a polite communication using very easy to understand explanations. This agent is analyzing the client request to identify possible problems he encounters. For each problem or explicite question, it identifies a possible known Expert on the related subject, and sends a question to this Expert. If no known expert if identified, it may build a short answer for its own. It also extracts some informations like the client name.
- the **Computer Expert** agent is analyzing the request from the first agent to identify a possible known question listed in a FAQ. If a known question is identified, it provides with the known procedure to solve the problem.
- the **Cooking Expert** agent is analyzing the request from the first agent to suggest a recipe, may be a new created one, and suggest a wine with it.

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

> Salut, c'est Slvy. Je voudrais me faire un hamburger, mais mon PC ne s'allume pas.

Click on the "Envoyer" button.

Wait for the responses, answer should be like:

> Bonjour Slvy,
> 
> Pour votre problème d'ordinateur qui ne s'allume pas, voici quelques étapes que vous pouvez suivre :
> 
> 1. Vérifiez si le câble d'alimentation est correctement connecté à l'ordinateur et à la prise de courant.
> 2. Assurez-vous que la prise de courant fonctionne en testant un autre appareil.
> 3. Appuyez fermement sur le bouton d'alimentation pendant au moins 5 secondes.
> 4. Si l'ordinateur ne s'allume toujours pas, essayez d'utiliser un autre câble d'alimentation.
> 5. Inspectez l'unité d'alimentation pour détecter tout dommage visible ou connexion lâche.
> 6. Si tout le reste échoue, consultez un technicien professionnel.
> 
> En ce qui concerne la préparation d'un hamburger maison, voici une recette simple :
> 
> 1. Préchauffez votre four à 180°C.
> 2. Formez 4 steaks avec 500g de viande hachée de bœuf, salez et poivrez de chaque côté.
> 3. Faites chauffer une poêle avec un peu d'huile. Une fois chaude, faites cuire les steaks pendant environ 3 minutes de chaque côté pour une cuisson à point. Ajoutez une tranche de fromage sur chaque steak et laissez fondre légèrement.
> 4. Pendant ce temps, coupez un oignon en fines rondelles et faites-le revenir dans une autre poêle avec un peu d'huile jusqu'à ce qu'il soit doré.
> 5. Coupez une tomate en rondelles et lavez quelques feuilles de laitue.
> 6. Coupez 4 pains à hamburger en deux et faites-les toaster légèrement au four.
> 7. Assemblez le hamburger : sur la base du pain, étalez un peu de ketchup, moutarde et mayonnaise. Ajoutez ensuite la laitue, une rondelle de tomate, le steak avec le fromage fondu, quelques rondelles d'oignon, puis refermez avec l'autre moitié du pain.
> 8. Servez immédiatement, éventuellement avec des frites maison.
> 
> Pour accompagner ce plat, je vous suggère un vin rouge léger et fruité, comme un Beaujolais ou un Pinot Noir.
> 
> J'espère que ces informations vous seront utiles. N'hésitez pas si vous avez d'autres questions.

Server side exchanges between the 2 agents should be like:
```
Question from Support Agent to ask_computer_expert Agent: Pourquoi un PC pourrait-il ne pas s'allumer ?
For this problem: Computer won't turn on
Follow these instructions:
- Check if the power cable is properly connected to the computer and the power outlet.
- Ensure the power outlet is working by testing another device.
- Press the power button firmly for at least 5 seconds.
- If the computer still doesn't turn on, try using a different power cable.
- Inspect the power supply unit for any visible damage or loose connections.
- If all else fails, consult a professional technician.

Question from Support Agent to ask_cooking_expert Agent: Quels sont les étapes pour faire un hamburger maison ?
Bien sûr, je peux vous aider avec cela. Voici une recette simple pour un hamburger maison.

Ingrédients :
- 500g de viande hachée de bœuf
- 4 pains à hamburger
- 4 tranches de fromage (cheddar ou emmental)
- 1 tomate
- 1 oignon
- Quelques feuilles de laitue
- Ketchup, moutarde, mayonnaise
- Sel, poivre

Étapes :
1. Préchauffez votre four à 180°C.
2. Formez 4 steaks avec la viande hachée, salez et poivrez de chaque côté.
3. Faites chauffer une poêle avec un peu d'huile. Une fois chaude, faites cuire les steaks pendant environ 3 minutes de chaque côté pour une cuisson à point. Ajoutez une tranche de fromage sur chaque steak et laissez fondre légèrement.
4. Pendant ce temps, coupez l'oignon en fines rondelles et faites-le revenir dans une autre poêle avec un peu d'huile jusqu'à ce qu'il soit doré.
5. Coupez la tomate en rondelles et lavez les feuilles de laitue.
6. Coupez les pains à hamburger en deux et faites-les toaster légèrement au four.
7. Assemblez le hamburger : sur la base du pain, étalez un peu de ketchup, moutarde et mayonnaise. Ajoutez ensuite la laitue, une rondelle de tomate, le steak avec le fromage fondu, quelques rondelles d'oignon, puis refermez avec l'autre moitié du pain.
8. Servez immédiatement, éventuellement avec des frites maison.

Pour accompagner ce plat, je vous suggère un vin rouge léger et fruité, comme un Beaujolais ou un Pinot Noir.
```
