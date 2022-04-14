import pydantic
import configparser
from configparser import ConfigParser

class LearningParamConfig(pydantic.BaseModel):
    C: pydantic.NonNegativeFloat

class AppConfig(pydantic.BaseModel):
    learning_param: LearningParamConfig

def load_config(path: str) -> AppConfig:
    """ """
    config: ConfigParser = configparser.ConfigParser()
    config.optionxform = str # type: ignore
    config.read(path)
    my_config_parser_dict = {s:dict(config.items(s)) for s in config.sections()}
    print(my_config_parser_dict)
    app_config = AppConfig(**my_config_parser_dict)
    return app_config
