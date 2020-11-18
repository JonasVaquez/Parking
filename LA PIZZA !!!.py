stock={tomate:50,fromage:30,champignon:12,jambon:2,anchois:5,olive:20,lardon:3,crème:8,oeuf:2}

class Commis:
    def verifStock(self,stock,pizza):
        
        if pizza.tomate>stock[tomate] and pizza.fromage>stock[fromage] and pizza.champignon>stock[champignon] and  pizza.jambon>stock[jambon] and pizza.anchois>stock[anchois] and pizza.olive>stock[olive] and pizza.lardon>stock[lardon] and pizza.crème>stock[crème] and pizza.oeuf>stock[oeuf]:
            return False  #le commis vérifie s'il a assez de stock pour la pizza demandé, s'il n'y en a pas assez, il renvoie False
        
        else:
            pizza.tomate-=stock[tomate] #sinon il transfère le stock nécéssaire au cuisinier
            pizza.fromage-=stock[fromage]
            pizza.champignon-=stock[champignon]
            pizza.jambon-=stock[jambon]
            pizza.anchois-=stock[anchois]
            pizza.olive-=stock[olive]
            pizza.lardon-=stock[lardon]
            pizza.crème-=stock[crème]
            pizza.oeuf-=stock[oeuf]
            return True