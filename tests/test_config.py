# from gestaltconfig.config import Config
from gestaltconfig.config import Config
#from .config import Config
#import gestaltconfig.config 

cfg: Config = Config()
cfg.path = "configs/config.yaml"

print(cfg["joker"])
