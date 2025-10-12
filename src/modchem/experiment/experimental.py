import threading
import os
import importlib.util
class BaseExperiment():
    """Базовый класс описания эксперимента"""
    def __init__(self):
        pass

    def init(self, title: str):
        print("Initialization experiment on thread...")

class Experiment(BaseExperiment):

    def __init__(self):
        super().__init__()
    
    def init(self, project):
        pass

    def before_init():
        print("Loading parameters before init...")
