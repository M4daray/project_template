from pathlib import Path
import os 
from typing import Final

__version__ = '0.1.0'

PATH_MODULE_FOLDER: Final[Path] = Path(__file__).resolve().parent
PATH_PACKAGE_FOLDER: Final[Path] = PATH_MODULE_FOLDER.parent.parent

PATH_GENERATED_FOLDER: Final[str] = os.path.join(PATH_PACKAGE_FOLDER, "generated")
PATH_CONFIG_FOLDER: Final[str] = os.path.join(PATH_MODULE_FOLDER, "resources")