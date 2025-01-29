## Description

This is a Python application that simulates an interaction between a client (human) and a technical support system made up of multiple collaborative AI agents:
- the client **Support** agent is dedicated to a polite communication using very easy to understand explanations. This agent is using the **Dispatcher** agent to analyze the client request and identify possible problems he encounters. For each problem or explicite question, the **Dispatcher** agent identifies a possible known Expert on the related subject, and sends a question to this Expert. The client **Support** agent then uses the Expert tips to build the final comprehensive answer for the client. If no known Expert is identified, it may build a short answer by its own. It also extracts some informations like the client name.
- the **Computer Expert** agent is analyzing the request from the **Dispatcher** agent to identify a possible known question listed in a FAQ. If a known question is identified, it provides with the known procedure to solve the problem.
- the **Cooking Expert** agent is analyzing the request from the **Dispatcher** agent to suggest a recipe, may be a new created one, and suggest a wine with it.

## Install dependencies
```
pip install -r requirements.txt
```

## Configuration
Update the **Config.py** file to define the model you want to use betwwen local intranet "Mistral, "Llama", "DeepSeek", "Lucie" or internet "ChatGPT"
- if you are using the ChatGPT internet configuration, your must have an ```openai_api_key.txt``` file containing a valid OpenAPI key.
- if you are using the Mistral or Llama intranet configurations, you must have an ```hf_token.txt``` file containing an HugginFace token to an account granted to use the models.

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
> Je suis désolé de vous entendre avoir des problèmes avec votre ordinateur. Avant de vous aider à préparer votre hamburger, je voudrais vous aider à résoudre ce problème.
> 
> Voici quelques étapes pour essayer de réparer votre ordinateur :
> 
> 1. Vérifiez que la corde d'alimentation est correctement connectée à votre ordinateur et à l'électrique.
> 2. Vérifiez que l'électrique fonctionne en essayant avec un autre appareil.
> 3. Appuyez sur le bouton de démarrage pendant au moins 5 secondes.
> 4. Si votre ordinateur ne s'allume toujours pas, essayez d'utiliser une autre corde d'alimentation.
> 5. Inspectez l'unité de puissance pour toute détérioration visible ou connexions détachées.
> 6. Si tout échoue, consultez un professionnel technique.
> 
> Une fois que votre ordinateur sera en fonctionnement, je peux vous aider à préparer votre hamburger. Voici une recette simple pour un hamburger français :
> 
> Ingrédients :
> 
> * 500g de viande hachée (préférablement de bœuf élevé en plein air)
> * 1 oignon petit, haché
> * 2 gousses d'ail, hachées
> * 1 cuillère à soupe de moutarde de Dijon
> * 1 cuillère à soupe de sauce Worcestershire
> * Sel et poivre à goût
> * 4 brioches
> * 4 tranches de fromage Brie
> * 4 tranches d'oignons caramélisés
> * Laitue ou salade
> * Mayonnaise
> * Huile d'olive
> 
> Instructions :
> 
> 1. Dans un grand bol, mélangez la viande hachée, l'oignon haché, l'ail haché, la moutarde de Dijon, la sauce Worcestershire, le sel et le poivre. Mélangez doucement pour ne pas sur-travailler la viande.
> 2. Formez la préparation en 4 boules égales, en faisant une petite dépression au centre de chaque boule.
> 3. Faites chauffer une poêle sur feu moyen-élevé et ajoutez un filet d'huile d'olive. Cuisez les boules pendant environ 4-5 minutes de chaque côté, ou jusqu'à ce qu'elles atteignent votre niveau de cuisson préféré.
> 4. Alors que les boules cuisent, faites légèrement griller les brioches dans le four ou sur une griddle.
> 5. Une fois les boules cuites, placez une tranche de fromage Brie sur chaque boule et laissez-le fondre légèrement.
> 6. Assemblez les hamburgers en étalant une fine couche de mayonnaise sur les brioches, suivie d'une couche de laitue ou de salade, d'une tranche d'oignons caramélisés, de la boule de viande, et de la brioche supérieure.
> 7. Servez avec vos frites préférées et un verre de Pinot Noir pour compléter les saveurs.
> 
> Bon appétit !

## Server side exchanges between the Dispatcher and the 2 Expert agents
```
Dispatcher:
 [
    ["Computer", "Why is the user's computer not turning on?"],
    ["Cooking", "How can I help the user make a hamburger?"]
]


##### Question from Dispatcher Agent to Computer Agent:
Why is the user's computer not turning on?

For this problem: Computer won't turn on
Follow these instructions:
- Check if the power cable is properly connected to the computer and the power outlet.
- Ensure the power outlet is working by testing another device.
- Press the power button firmly for at least 5 seconds.
- If the computer still doesn't turn on, try using a different power cable.
- Inspect the power supply unit for any visible damage or loose connections.
- If all else fails, consult a professional technician.


##### Question from Dispatcher Agent to Cooking Agent:
How can I help the user make a hamburger?

 To create a traditional French-inspired gourmet hamburger, let's focus on using high-quality ingredients and adding a touch of French flair. Here's a simple recipe for a delicious French-style hamburger:

Ingredients:
1. 500g ground beef (preferably grass-fed)
2. 1 small onion, finely chopped
3. 2 cloves garlic, minced
4. 1 tablespoon Dijon mustard
5. 1 tablespoon Worcestershire sauce
6. Salt and pepper to taste
7. 4 brioche buns
8. 4 slices of Brie cheese
9. 4 slices of caramelized onions
10. Arugula or lettuce
11. Mayonnaise
12. Olive oil

Instructions:
1. In a large bowl, combine the ground beef, chopped onion, minced garlic, Dijon mustard, Worcestershire sauce, salt, and pepper. Mix gently to avoid overworking the meat.
2. Form the mixture into 4 equal-sized patties, making a slight indentation in the center of each one.
3. Heat a large skillet over medium-high heat and add a drizzle of olive oil. Cook the patties for about 4-5 minutes on each side, or until they reach your desired level of doneness.
4. While the patties are cooking, lightly toast the brioche buns in the oven or on a griddle.
5. Once the patties are cooked, place a slice of Brie cheese on each one and let it melt slightly.
6. Assemble the burgers by spreading a thin layer of mayonnaise on the buns, followed by a layer of arugula or lettuce, a caramelized onion slice, the cheesy burger patty, and the top bun.
7. Serve with your favorite French fries and a glass of Pinot Noir to complement the flavors.

Enjoy your French-style gourmet hamburger!

#### All dispatches done ####
```
