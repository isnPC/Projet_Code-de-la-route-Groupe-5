import random
from random import randint
import tkinter as tk
from PIL import Image, ImageTk



def lectureQuesRep(borneQuesRep):
    """Ouvre le fichier des bornes de réponses et renvoie une liste dont chaque élément correspond à une question et ses paramétres"""
    fichier = open(borneQuesRep, "r")
    listeQuestion = []
    for ligne in fichier:
        listeQuestion.append(ligne)
    return listeQuestion

def aleaQues(borneQuesRep):
    """choisi un élément aléatoire de la liste et le renvoie"""
    listeQuestion = lectureQuesRep(borneQuesRep)
    random.shuffle(listeQuestion)
    return listeQuestion

def choixQues(paramQues):
    """renvoie une liste dont chaque élément correspond a un paramètre"""
    question = paramQues.split(';')
    return question


def affichage(question):
    """affiche la question et les propositions du paramètre question"""
    print(question[0])
    print(question[1])
    print(question[2])
    if question[3] != "":
        print(question[3])
    if question[4] != "":
        print(question[4])


def afficheRep(question):
    """pouvoir ecrire sa reponse et affiche si la reponse est vraie ou fausse"""
    reponse = input("Quel est votre réponse?") #permet de rentrer sa reponse
    if testReponse(question,reponse) == True:
        print("Bonne réponse!")
    else:
        print("FAUX!")
    print(question[6])
    return reponse


def testReponse(question, reponse):
        """verifie si la reponse est juste, renvoie True ou fausse et renvoie False"""
        if reponse == question[5]:
            return True
        else:
            return False


def pointsrepFausses(reponse, repFausses):
    """si la reponse a la question posé est fausse, le nombre reponses fausse augment de 1, sinon le nombre de reponse fausse ne change pas"""
    if testReponse(question,reponse) == False:
        repFausses = repFausses+1
        return repFausses
    else:
        repFausses = repFausses
        return repFausses


def singPlur(repFausses):
    """si le nombre de reponse fausse est superieur a 1, le mot fautes'accorde au pluriel"""
    if repFausses <= 1:
        return "faute"
    else:
        return "fautes"


def afficher_image(nomImg):
    """affiche l'image correspondante a la question posée"""
    window = tk.Tk()
    image = Image.open(nomImg)
    photo = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width = image.size[0], height = image.size[1])
    canvas.create_image(0,0, anchor = tk.NW, image=photo)
    canvas.pack()
    window.mainloop()



# test fonctions
borneQuesRep = "quesRep.txt"
nbQues = 0
repFausses = 0
lectureQuesRep(borneQuesRep)
listeQuestion = aleaQues(borneQuesRep)

while nbQues != 10:
    numQuestion = randint(1,len(listeQuestion))
    paramQues = listeQuestion[numQuestion-1]
    question = choixQues(paramQues)
    affichage(question)
    listeQuestion.remove(paramQues)
    nomImg = question[7]
    afficher_image(nomImg)
    reponse = afficheRep(question)
    testReponse(question, reponse)
    repFausses = pointsrepFausses(reponse, repFausses)
    nbQues = nbQues+1
print("Vous avez fait", repFausses, "fautes sur", nbQues, "questions")