from jinja2 import FileSystemLoader, Environment
from pathlib import Path
import os

def load_app_template():
    env = Environment(loader=FileSystemLoader(Path(__file__).parent))
    temp = env.get_template("app.py-tpl")
    render_code = temp.render({"APP_DIR": os.getenv("MODCHEM_APP_NAME")})

    with open(os.path.join(os.getcwd(), os.getenv("MODCHEM_APP_NAME"), "app.py"), "w") as file:
        file.write(render_code)

def load_params_template():
    env = Environment(loader=FileSystemLoader(Path(__file__).parent))
    temp = env.get_template("params.py-tpl")
    render_code = temp.render()
    with open(os.path.join(os.getcwd(), os.getenv("MODCHEM_APP_NAME"), "params.py"), "w") as file:
        file.write(render_code)
