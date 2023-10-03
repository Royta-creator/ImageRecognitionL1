# L1-projects Tensorflow
L1 Project 2023 - 2024

Reconnaissance d'image :

Introduction :

Ce projet a pour objectif de concevoir un script de reconnaissance d'images en utilisant Python. Le chatbot communique par texte reconnaissant des éléments dans des images fournies par l'utilisateur.

Aperçu du projet :

Le projet combine des éléments de développement d'interface utilisateur graphique (GUI) avec Tkinter, d'apprentissage automatique (TensorFlow et Keras), et de conversion texte-voix (pyttsx3). Le chatbot permet aux utilisateurs d'interagir et de lui demander de reconnaître des éléments dans des images.

Contexte et motivation :

La motivation derrière le projet est d'exploiter les capacités de reconnaissance d'images d'un modèle de reconnaissance d'image pré-entraîné à l'aide d'un chatbot, offrant ainsi une manière accessible aux utilisateurs d'identifier des éléments sur des images.

Technologies utilisées :

- Tkinter pour le développement de l'interface utilisateur graphique.
- TensorFlow et Keras pour l'apprentissage automatique et la reconnaissance d'images.
- pyttsx3 pour la conversion texte-voix.
- ChatGPT pour la réalisation du modèle utilisant InceptionV3 (une architecture de réseau neuronal convolutif (CNN)) et ImageNet (base de données).

Architecture :

Le projet a une structure modulaire avec des fonctions distinctes pour l'initialisation de la conversion texte-voix, le chargement du modèle InceptionV3, le prétraitement des images, la prédiction des éléments, et la mise en œuvre du chatbot.

Implémentation :

Le script initialise un moteur de conversion texte-voix, charge le modèle InceptionV3 avec des poids pré-entraînés, et définit des fonctions pour le prétraitement des images et la prédiction des éléments. La fonction du chatbot interagit avec l'utilisateur via l'entrée de la console. Elle reconnaît des commandes telles que 'quit' pour quitter et 'recognize image' pour initier la reconnaissance d'images. Cependant, le chatbot ne possède pas d'intelligence réelle et ne peut reconnaître qu'un nombre restreint d'inputs de l'utilisateur.

Défis rencontrés :

Le projet devait à la base se faire sans l'utilisation de TensorFlow en se basant sur le modèle du perceptron et la descente de gradient. Cependant, le processus d'entraînement devenait laborieux avec des résultats peu convaincants. TensorFlow et ses bases de données beaucoup plus conséquentes ainsi que ses modèles pré-entraînés étaient alors beaucoup plus efficaces en plus d'avoir des librairies plus simples à manipuler. De plus, en ce qui concerne le chatbot, il reste très limité, notamment avec une incapacité à traiter des saisies de l'utilisateur différentes de celles connues.

Tests et validation :

Le projet peut être testé en exécutant le script, en interagissant avec le chatbot et en fournissant des images pour la reconnaissance. La validation implique de vérifier que le chatbot reconnaît correctement les éléments sur les images et répond de manière appropriée.

Résultats :

Le principal résultat est la capacité du chatbot à reconnaître des éléments dans des images fournies par l'utilisateur et à communiquer les résultats à la fois via la sortie de la console et par la voix.

Conclusion :

Le projet combine avec succès l'interface graphique, l'apprentissage automatique, et la conversion texte-voix pour créer un chatbot de reconnaissance d'images. Il sert de base pour de futurs développements à la fois dans la reconnaissance d'images et dans les fonctionnalités des chatbots.

Références :

Le projet fait référence aux bibliothèques Tkinter, TensorFlow, Keras, et pyttsx3 pour le développement de l'interface graphique, l'apprentissage automatique, et les fonctionnalités de conversion texte-voix. Ainsi qu'au modèle InceptionV3 et à la base de données ImageNet.


Roy TAMWO
