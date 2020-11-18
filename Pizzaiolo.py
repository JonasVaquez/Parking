from commis import *

Marguerita = Pizza (1,1,1,0,0,0,0,0,0)
Roma = Pizza (1,0,1,1,0,0,0,0)
Napolitaine = Pizza (1,1,0,0,1,1,0,0)
Toscane = Pizza (1,1,1,0,0,0,1,1,1)
Calzone = Pizza (1,1,1,1,0,0,0,0,1)
Royale = Pizza (1,1,1,1,0,0,1,1,1)

class Pizza:
    """Classe dans laquelle les ingrédients nécessaires pour confectionner une
    pizza sont inscrits"""
        
    def __init__(self,tomate, fromage, champignon, jambon, anchois, olive, lardon, crème, oeuf):
        """création de la liste d'ingrédients nécessaires pour la pizzeria"""
        self.tomate = tomate
        self.fromage = fromage
        self.champignon = champignon
        self.jambon = jambon
        self.anchois = anchois
        self.olive = olive
        self.lardon = lardon
        self.crème = crème
        self.oeuf = oeuf
  
class Pizzaiolo:
    """Classe dans laquelle le Pizzaiolo intéragit avec son client et
    confectionne,ou non, la pizza"""
    def commande(pizza,commis):
        """Fonction qui vérifie le stock et confectionne la pizza en faisant
           patienter le client, ou l'avertit si il ne peut pas faire la
           pizza par manque d'ingrédients"""
        if commis.verifStock(pizza) == True:            #vérifie le stock
            f"Je vous prépare votre pizza !"    #soustrait les ingrédients utilisés au sotck et avertit le client de la confectioin de la pizza    
        else :
            f"Je suis désolé, mais je n'ai plus les ingrédients nécessaires pour faire votre pizza. Commnderez vous autre chose ?"
            commis.commande(stock, 5)                 #commande au commis le stock nécessaire pour faire la pizza demandée par le client et avertit le client que la pizza est indisponible 

