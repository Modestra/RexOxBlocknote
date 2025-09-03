from redox.catalogs.elements import ElementList
from redox.entities.atom import Atom, AtomList
from events import Events
class Ion:
    atom_list: dict[str, AtomList] = {}
    count: int = 0
    def __init__(self, ion, count):
        self.ion = ion
        self.count = count
        self.atom_list = {}
        self.atom_list[ion] = AtomList(Atom("S"), count)

    def __str__(self):
        return str(self.__dict__)

    def info(self):
        return self.atom_list
    
    def append_atom(self, el_name: str, atom_count: int):
        self.atom_list.update({el_name: AtomList(Atom(el_name), atom_count)})

