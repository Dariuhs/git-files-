
#Voici un exemple de code Python qui intègre pour chaque aspect de la gestion de l'université, un code SQL basique pour stocker les informations dans une base de données :


import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('universite.db')

# Classe pour représenter un étudiant
class Etudiant:
    def __init__(self, nom, prenom, email, matricule):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.matricule = matricule
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO etudiants (nom, prenom, email, matricule) VALUES (?, ?, ?, ?)', (self.nom, self.prenom, self.email, self.matricule))
        conn.commit()

# Classe pour représenter un enseignant
class Enseignant:
    def __init__(self, nom, prenom, email, bureau, matricule):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.bureau = bureau
        self.matricule = matricule
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO enseignants (nom, prenom, email, bureau, matricule) VALUES (?, ?, ?, ?, ?)', (self.nom, self.prenom, self.email, self.bureau, self.matricule))
        conn.commit()

# Classe pour représenter un cours
class Cours:
    def __init__(self, nom, code, enseignant, salle, heure):
        self.nom = nom
        self.code = code
        self.enseignant = enseignant
        self.salle = salle
        self.heure = heure
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO cours (nom, code, enseignant, salle, heure) VALUES (?, ?, ?, ?, ?)', (self.nom, self.code, self.enseignant, self.salle, self.heure))
        conn.commit()

# Classe pour représenter un programme
class Programme:
    def __init__(self, nom, code, cours):
        self.nom = nom
        self.code = code
        self.cours = cours
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO programmes (nom, code, cours) VALUES (?, ?, ?)', (self.nom, self.code, self.cours))
        conn.commit()

# Classe pour représenter les finances
class Finances:
    def __init__(self, budget_annuel):
        self.budget_annuel = budget_annuel
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO finances (budget_annuel) VALUES (?)', (self.budget_annuel,))
        conn.commit()

# Classe pour représenter les installations
class Installations:
    def __init__(self, nom, localisation, capacite):
        self.nom = nom
        self.localisation = localisation
        self.capacite = capacite
        
    def sauvegarder(self):
        c = conn.cursor()
        c.execute('INSERT INTO installations (nom, localisation, capacite) VALUES (?, ?, ?)', (self.nom, self.localisation, self.capacite))
        conn.commit()

# Classe pour représenter les ressources humaines
class RessourcesHumaines:
    def __init__(self, nom, prenom, poste, salaire):
        self.nom = nom
        self.p