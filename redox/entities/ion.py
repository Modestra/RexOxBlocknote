from typing import Any
import json
from redox.catalogs.elements import ElementList
from redox.entities.atom import Atom, AtomList
class Ion:
    atom_list: dict[str, AtomList] = {}
    count: int = 0
    def __init__(self, ion, count):
        self.ion = ion
        self.count = count
        pass

    def __str__(self):
        return str(self.__dict__)
    
    def append_atom(self, el_name: str, atom_count: int):
        self.atom_list.update({el_name: AtomList(Atom("H"), atom_count)})
