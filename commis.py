stock={'tomate':50,'fromage':30,'champignon':12,'jambon':2,'anchois':5,'olive':20,'lardon':3,'crème':8,'oeuf':2}

class Commis:
    
    def verifStock(stock,pizza):
        
        if pizza.tomate>stock['tomate'] or pizza.fromage>stock['fromage'] or pizza.champignon>stock['champignon'] or  pizza.jambon>stock['jambon'] or pizza.anchois>stock['anchois'] or pizza.olive>stock['olive'] or pizza.lardon>stock['lardon'] or pizza.crème>stock['crème'] or pizza.oeuf>stock['oeuf']:
            return False  #le commis vérifie s'il a assez de stock pour la pizza demandé, s'il n'y en a pas assez, il renvoie False
        
        else:
            stock['tomate']-=pizza.tomate #sinon il transfère le stock nécéssaire au cuisinier
            stock['fromage']-=pizza.fromage
            stock['champignon']-=pizza.champignon
            stock['jambon']-=pizza.jambon
            stock['anchois']-=pizza.anchois
            stock['olive']-=pizza.olive
            stock['lardon']-=pizza.lardon
            stock['crème']-=pizza.crème
            stock['oeuf']-=pizza.oeuf
            return True
       
     def Commande(self,stock,quantite): #achète des ingrédients pour remplir le stock
            stock['tomate']+=quantite
            stock['fromage']+=quantite
            stock['champignon']+=quantite
            stock['jambon']+=quantite
            stock['anchois']+=quantite
            stock['olive']+=quantite
            stock['lardon']+=quantite
            stock['crème']+=quantite
            stock['oeuf']+=quantite
