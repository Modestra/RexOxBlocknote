import unittest
from modchem.core.project import Project

class TestProjectMethods(unittest.TestCase):

    def test_create_project(self):
        self.assertEqual(Project(name="Testing").get_config(), {"name": "Testing"})