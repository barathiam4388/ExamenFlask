class Vehicule:
    def __init__(self, marque, modele, id_vehicule, disponibilite="Disponible"):
        self.marque = marque
        self.modele = modele
        self.id_vehicule = id_vehicule
        self.disponibilite = disponibilite
    
    def afficher_info(self):
        return f"ID: {self.id_vehicule}, Marque: {self.marque}, Modèle: {self.modele}, Disponibilité: {self.disponibilite}"
    
    def changer_statut_disponibilite(self, statut):
        self.disponibilite = statut

class Location:
    def __init__(self):
        self.vehicules = {}
    
    def ajouter_vehicule(self, vehicule):
        self.vehicules[vehicule.id_vehicule] = vehicule
    
    def supprimer_vehicule(self, id_vehicule):
        if id_vehicule in self.vehicules:
            del self.vehicules[id_vehicule]
    
    def rechercher_vehicule(self, id_vehicule):
        return self.vehicules.get(id_vehicule, None)
    
    def afficher_vehicules_disponibles(self):
        for vehicule in self.vehicules.values():
            if vehicule.disponibilite == "Disponible":
                print(vehicule.afficher_info())
    
    def reserver_vehicule(self, id_vehicule):
        vehicule = self.rechercher_vehicule(id_vehicule)
        if vehicule:
            vehicule.changer_statut_disponibilite("Réservé")
            
        
