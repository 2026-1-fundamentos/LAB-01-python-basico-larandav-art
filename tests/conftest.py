import os
import sys

# Agrega homework al path y cambia el directorio de trabajo
homework_path = os.path.join(os.path.dirname(__file__), "..", "homework")
os.chdir(os.path.abspath(homework_path))
sys.path.insert(0, os.path.abspath(homework_path))