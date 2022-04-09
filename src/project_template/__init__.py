from pathlib import Path
import os 

__version__ = '0.1.0'

PATH_MODULE_FOLDER: Path = Path(__file__).resolve().parent
PATH_PACKAGE_FOLDER: Path = PATH_MODULE_FOLDER.parent.parent

PATH_GENERATED_FOLDER: str = os.path.join(PATH_PACKAGE_FOLDER, "generated")
PATH_CONFIG_FOLDER: str = os.path.join(PATH_MODULE_FOLDER, "resources", "config.yaml")