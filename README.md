# Cryptographie

## Procédure
1. Récupérer l'image Docker et lancer le conteneur
```
sudo docker run -dp 5000:5000 ceiko/cryptography
```

2. Ouvrir un navigateur web et se rendre à l'url suivante :
```
http://localhost:5000/
```

## Utilisation de l'interface WEB
Afin d'utiliser une interface WEB, ouvrir un navigateur Web à l'URL décrite plus haut.  
Enfin, remplir les différents champs en fonction de ce que vous souhaitez faire.  

## Quelques exemples API
### Préambule
Il est également possible de faire des requêtes sans passer par une interface WEB.  
Pour ce faire, l'URL de base est la suivante :
```
http://localhost:5000/api
```

### Liste des paramètres à utiliser en fonction des algorithmes :

#### Analyse fréquentielle  
algo=frequence  
texte=&lt;texte_a_analyser&gt;  
action=analyse  
  
Exemple :  
```
http://localhost:5000/api?algo=frequence&texte=sdf+sdg++dh+sgtdfh++jkrtrsviospvh+qp+yvgzpsy+ho+qemifgqhewoh+qreihogesuhgzqepiqgherghqzmg+ohsrhemrghoqelqmsoyy%22haozaz&action=analyse
```

#### Algorithme de César  
1. Chiffrement de texte :  
algo=cesar  
decalage=&lt;nombre_entier&gt;  
texte=&lt;texte_a_chiffrer&gt;  
action=chiffrer   
  
Exemple : 
```
http://localhost:5000/api?algo=cesar&decalage=-3&texte=securite&cle=&crypte=&action=chiffrer
```
  
2. Déchiffrement de texte :  
algo=cesar  
decalage=&lt;nombre_entier&gt;  
crypte=&lt;texte_a_dechiffrer&gt;  
action=dechiffrer  
   
Exemple : 
```
http://localhost:5000/api?algo=cesar&decalage=-3&texte=&cle=&crypte=PBZROFQB&action=dechiffrer
``` 

#### Algorithme de Vigenere  
1. Chiffrer un texte :  
algo=vigenere  
texte=&lt;texte_a_chiffrer&gt;
cle=&lt;cle_pour_chiffrer&gt;  
action=chiffrer  
  
Exemple : 
```
http://localhost:5000/api?algo=vigenere&texte=dCode+Vigenere+automatiquement&cle=cle&action=chiffrer
```

2. Déchiffer un texte :  
algo=vigenere  
cle=&lt;cle_pour_dechiffrer&gt;
crypte=&lt;texte_a_dechiffrer&gt;  
action=dechiffrer  
  
Exemple : 
```
http://localhost:5000/api?algo=vigenere&cle=securite&crypte=BI+O%27UGXXPDI+FUEAHOG+GJYZSGE&action=dechiffrer
```



