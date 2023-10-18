class auto:
    def __init__(self,marca,modello,targa,km_percorsi):
        self.marca=marca
        self.modello=modello
        self.targa=targa
        self.km_percorsi=km_percorsi

    def effettua_viaggio(self,km):
        self.km_percorsi=self.km_percosi+km


auto1=auto("bmw","m4","fyh5j4",146349)
auto1.effettua_viaggio(10)
print(auto1.km_percorsi)