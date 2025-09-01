from redox.catalogs.elements import ChemicalPartical, ELEMENTS
class Atom(ChemicalPartical):
    atom_name: str
    def __init__(self, atom_name: str):
        self.atom_name = atom_name
    
    def __str__(self):
        return str(ELEMENTS[self.atom_name].__dict__)
    

class AtomList:
    atom: Atom
    count: int

    def __init__(self, atom: Atom, count: int):
        self.atom = atom
        self.count = count
    
    def get_list(self):
        return {self.atom.atom_name: self.atom, "count": self.count}