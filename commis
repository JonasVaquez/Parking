stock={'tomate':50,'fromage':30,'champignon':12,'jambon':2,'anchois':5,'olive':20,'lardon':3,'crème':8,'oeuf':2}

class Commis:
    
    def verifStock(self,stock,pizza):
        
        if pizza.tomate>stock['tomate'] or pizza.fromage>stock['fromage'] or pizza.champignon>stock['champignon'] or  pizza.jambon>stock['jambon'] or pizza.anchois>stock['anchois'] or pizza.olive>stock['olive'] or pizza.lardon>stock['lardon'] or pizza.crème>stock['crème'] or pizza.oeuf>stock['oeuf']:
            return False  #le commis vérifie s'il a assez de stock pour la pizza demandé, s'il n'y en a pas assez, il renvoie False
        
        else:
            pizza.tomate-=stock['tomate'] #sinon il transfère le stock nécéssaire au cuisinier
            pizza.fromage-=stock['fromage']
            pizza.champignon-=stock['champignon']
            pizza.jambon-=stock['jambon']
            pizza.anchois-=stock['anchois']
            pizza.olive-=stock['olive']
            pizza.lardon-=stock['lardon']
            pizza.crème-=stock['crème']
            pizza.oeuf-=stock['oeuf']
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
