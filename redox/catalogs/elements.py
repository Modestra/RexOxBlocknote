class Element:
    def __init__(self, symbol, name, atom_mass, electronegativity):
        self.symbol = symbol
        self.name = name
        self.atom_mass = atom_mass
        self.electronegativity = electronegativity
    
    def __str__(self):
        return str(self.name)
    
    def get_atom_mass(self):
        return self.atom_mass

    def get_element_info(self, symbol):
        return ELEMENTS[symbol]
    
ELEMENTS = {
    'H': Element('H', 'Водород', 1.00794, 2.2),
    'He': Element('He', 'Гелий', 4.002602, 0),
    'Li': Element('Li', 'Литий', 6.941, 0.93),
    'Be': Element('Be', 'Бериллий', 9.01218, 1.5),
    'B': Element('B', 'Бор', 10.811, 2.0),
    'C': Element('C', 'Углерод', 12.011, 2.5),
    'N': Element('N', 'Азот', 14.0067, 3.0),
    'O': Element('O', 'Кислород', 15.9994, 3.5),
    'F': Element('F', 'Фтор', 18.998403, 4.0),
    'Ne': Element('Ne', 'Неон', 20.179, 0),
    'Na': Element('Na', 'Натрий', 22.98977, 0.9),
}

class ElementList:
    """Массив с постоянными значениями для элементов"""
    def elements_list():
        result = {}
        for element in ELEMENTS.keys():
            result[element] = ELEMENTS[element].__dict__
        return result

class ChemicalPartical():
    """Базовый класс для описания физико-химических параметров макрочастиц"""
    atom_name: str
    def __init__(self):
        pass

class BaseChemicalParticalList():
    """Базовый класс для описания взаимодейсвия между частицами"""
    def __init__(self):
        pass

