# Importation des bibliothèques nécessaires
import numpy as np          # Pour les calculs mathématiques
import random              # Pour générer des nombres aléatoires
from rich import print     # Pour un affichage coloré dans le terminal
import os                  # Pour les opérations système
import pandas as pd        # Pour la manipulation de données

class Morpion:
    """
    Classe qui implémente le jeu du Morpion (Tic-tac-toe).
    
    Le jeu utilise un dictionnaire pour représenter le plateau où :
    - Les clés sont les positions de '1' à '9'
    - Les valeurs possibles sont :
        ' ' = case vide
        'X' = coup du joueur humain
        'O' = coup de l'IA
    
    Structure du plateau :
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9
    """
    def __init__(self):
        # Initialisation du plateau comme un dictionnaire vide
        self.plateau = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ','7':' ','8':' ','9':' '}
        # Liste des coups disponibles (positions non occupées)
        self.coups_possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def reinitialiser(self):
        """
        Réinitialise le plateau et la liste des coups possibles pour une nouvelle partie.
        
        Returns:
            dict: Le plateau vide initialisé
        """
        self.plateau = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ','7':' ','8':' ','9':' '}
        self.coups_possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return self.plateau

    def mouvements_disponibles(self):
        """
        Retourne la liste des positions disponibles sur le plateau.
        Cette méthode n'est actuellement pas utilisée mais pourrait être utile
        pour des améliorations futures.
        
        Returns:
            list: Liste des coordonnées (i,j) des cases vides
        """
        return [(i, j) for i in range(3) for j in range(3) if self.plateau[i, j] == 0]

    def jouer_coup(self, position, joueur):
        """
        Effectue un coup sur le plateau si la position est valide.
        
        Args:
            position (int): Position choisie (1-9)
            joueur (int): Identifiant du joueur (1 pour l'IA, 2 pour l'humain)
        
        Returns:
            tuple: (plateau actualisé, liste des coups encore possibles)
        """
        if position in self.coups_possibles:
            # L'IA joue avec 'O'
            if joueur == 1:
                self.plateau[str(position)] = 'O'
                self.coups_possibles.remove(position)
            # Le joueur humain joue avec 'X'
            elif joueur == 2:
                self.plateau[str(position)] = 'X'
                self.coups_possibles.remove(position)
        else:
            print('Veuillez entrer une position valide')
            
        return self.plateau, self.coups_possibles

    def verifier_gagnant(self):
        """
        Vérifie s'il y a un gagnant sur le plateau.
        Examine toutes les combinaisons gagnantes possibles pour les deux symboles.
        
        Returns:
            str: 'X' si le joueur gagne, 'O' si l'IA gagne, None sinon
        """
        for symbole in ['X', 'O']:
            # Liste des combinaisons gagnantes (lignes, colonnes, diagonales)
            combinaisons_gagnantes = [
                (1, 2, 3), (1, 4, 7),  # Première ligne et première colonne
                (7, 8, 9), (3, 6, 9),  # Dernière ligne et dernière colonne
                (1, 5, 9), (3, 5, 7),  # Diagonales
                (2, 5, 8), (4, 5, 6)   # Ligne et colonne du milieu
            ]
            for combo in combinaisons_gagnantes:
                if (self.plateau[str(combo[0])] == symbole and 
                    self.plateau[str(combo[1])] == symbole and 
                    self.plateau[str(combo[2])] == symbole):
                    return symbole

    def afficher_plateau(self, gagnant=''):
        """
        Affiche le plateau de jeu dans le terminal avec une mise en forme colorée.
        Affiche également le résultat de la partie si elle est terminée.
        
        Args:
            gagnant (str): Le symbole du gagnant ('X', 'O' ou vide pour partie en cours)
        """
        # Création d'un dictionnaire avec les symboles colorés en rouge
        plateau_colore = {
            pos: pos if valeur == ' ' else f"[red]{valeur}[/red]" 
            for pos, valeur in self.plateau.items()
        }
        
        # Construction de l'affichage du plateau
        affichage = (
            f"     |     |     \n"
            f"  {plateau_colore['1']}  |  {plateau_colore['2']}  |  {plateau_colore['3']}\n"
            f"_____|_____|_____\n"
            f"     |     |     \n"
            f"  {plateau_colore['4']}  |  {plateau_colore['5']}  |  {plateau_colore['6']}\n"
            f"_____|_____|_____\n"
            f"     |     |     \n"
            f"  {plateau_colore['7']}  |  {plateau_colore['8']}  |  {plateau_colore['9']}\n"
            f"     |     |     "
        )
        
        # Affichage du plateau
        print(affichage)
        
        # Affichage du résultat si la partie est terminée
        if gagnant == 'X':
            print(f"Vous avez gagné! 🎉")
        elif gagnant == 'O':
            print(f"L'IA a gagné! 😢")
        elif all(i != ' ' for i in self.plateau.values()):  # Vérifie si toutes les cases sont remplies
            print(f"Match nul! 🤝")

if __name__ == "__main__":
    m = Morpion()
