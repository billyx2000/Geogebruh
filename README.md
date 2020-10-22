# Geogebruh
Projet generation de graphique dynamique, d'expression mathematique entré par un utilisateur

## Parties

**Les parties peuvent etre modifiées/ameliorées**

* User GUI and User input (return **string**)
	* Description : Generation de la fenetre d'action avec un graphique par defaut et des champs de saisie utilisateur pour entrer la fonction, les intervalles et le pas (step) utilisé pour génerer le graphique
		* *range_min = MIN*
		* *range_max = MAX*
		* *range_step = STEP*
	* Main : **@Graham** / **@Milan**
	* Second : ?
	* File : *tests/test_implementation.py*

* Analyse lexical/syntaxique (return **array**)
	* Description : Découpage en tokens de l'expression mathematique entré par l'utilisateur, et assignation des attributs (OPERATEUR/NOMBRE/FONCTION/STRUCTURE/VARIABLE) pour permettre la verification par le **Evaluateur**
		* **OPERATEUR**	: *+, -, *, /*
		* **NOMBRE**	: *e.g. 1, 74, 26*
		* **FONCTION**	: *sin, cos, tan, pow, abs, sqrt, log, fctr (factoriel)*
		* **STRUCTURE**	: *e.g. ( ) [ ]*
		* **VARIABLE**	: *e.g. x (Defined at the start, to simplify the process)*
	* Main : **@Milan**
	* Second : ?
	* File : *lexical_analysis.py*

* Evaluateur (return **f(x)**)
	* Description : Verification des tokens avec les valeurs/structures/fonctions supportés (sin, cos, ...) et concatenation de l'array pour l'execution
	* Main : ?
	* Second : ?

* Generation du graphique
	* Description : 
	* Main : ?
	* Second : ?

