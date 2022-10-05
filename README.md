
# Modélisation et résolution

*Le projet est à faire par groupe. Vous devrez rendre **un rapport**, ainsi que **les sources** des différents modèles.
Vous **présenterez** également votre travail lors de la dernière séance de ce module **(15/12/2022)**.*

## Exercice 1 (Etiquetage de graphe et ”cyclic-bandwidth problem”)

Un graphe G est un couple (V(G), E(G))
> V(G) : ensemble appelé ensemble de sommets
>
> E(G) : ensemble de paires d’éléments de V(G) appelé ensemble des arêtes
>
> G = (V(G), E(G)) : un graphe
> 
> n = #V(G) : nombre de sommets de V(G)).

Un étiquetage f d’un graphe G est une fonction bijective de V(G) dans
{1, . . . , n}, c’est-à-dire, f : V(G) → {1, . . . , n}.

> Soit G un graphe
> 
> f un étiquetage de G
> 
> (u, v) une arête de G

On appelle distance entre u et v le nombre 
> |f (v)−f (u)|

(où |x| représente la valeur absolue de x).

La ”cyclic-bandwidth” du graphe G par rapport à l’étiquetage f est donnée par

> CB(G, f ) = max(u,v)∈E(G){min{|f(v) − f(u)|, n − |f(v) − f(u)|}}

Le ”cyclic-bandwidth problem”
consiste à trouver l’étiquetage g tel que

> CB(G, g) = minf ∈E {CB(G, f )}

où E représente l’ensemble des étiquetages.

1. Trois modélisations (papier) sont demandées :
   
   - **M1** : un modèle pour minimiser la cyclic-bandwidth basé sur des variables ”domaine fini” entières (FD);

   - **M2** : un modèle basé également sur des variables ”domaine fini” entières (FD), mais avec une approche très différente de M1, sans contrainte “arithmétique”, et s’intéressant à la satisfaction (i.e., recherche d’un étiquetage de cyclic-bandwidth de valeur k donnée);

   - **M3** : un modèle basé sur des variables booléennes et contraintes booléennes (SAT), s’intéressant à la satisfaction (i.e., recherche d’un étiquetage de cyclic-bandwidth de valeur k donnée). Analyser et comparer les différents modèles, en terme de nombre de contraintes, de nombre de variables, de complexité des contraintes, etc.

2. Pour chacun des modèles **M1** à **M3**, proposer des idées et les réaliser pour **casser de possibles symmétries**
(et donc éliminer des solutions symmétriques). Comparer les possibilités entre les différents modèles.

3. La “programmation” des modèles se fera en **PyCSP3** (ou MiniZinc) pour les modèles **M1** et **M2**, et en **PySAT** (ou génération directe de DIMACS) pour le modèle **M3**. La résolution se fera avec le solveur de
votre choix, de préférence ACE pour les domaines finis en PyCSP3, Gecode pour les modèles domaines
finis en MiniZinc, et Glucose ou MiniSAT pour le booléen. Analyser et comparer les différentes solutions que vous aurez proposées en utilisant certains des graphes (ou tous) du benchmark Harwell-Boeing 113 (sous Moodle). Cette question peut être abordée de nombreuses façons, à vous de choisir l’étude à mener. Ne pas oublier que pour **M2** et **M3** il est possible d’encadrer la valeur optimale, voire de la trouver dans certains cas.

4. Complèter ou utiliser **M2** et **M3** pour calculer la cyclic-bandwidth optimale. Décrire l’algorithme et l’implanter. Analyser et comparer les résultats sur les instances précédentes. Il est possible d’imaginer des
solutions parallèles.

# Docs sur la cyclic-bandwidth
- https://hal.archives-ouvertes.fr/hal-01392218
- https://hal.archives-ouvertes.fr/hal-01166658/document