

import pickle

def sauvegarde(variable,fichier):
    """cette fonction permet de sauvegarder une variable dans un fichier"""
    outfile = open(fichier,'wb')
    pickle.dump(variable,outfile)
    outfile.close()

score=[0,0,0,0,0,0,0,0,0,0] #il y a 10 zéros qui vont remplacer les meilleurs scores
print(score)
sauvegarde(score,"fichier_meilleurs_scores_tetris")