from gestaltconfig.singleton import Singleton
from pathlib import Path

from typing import Any, Dict

import yaml


class Config(Singleton):
    def __init__(self):
        Singleton.__init__(self)
        self._path = ""  # path to config file

    def __getitem__(self, key):
        return self._cfg[key]

    def __setitem__(self, key, value):
        self._cfg[key] = value

    def __repr__(self):
        return repr(self._cfg)

    def __str__(self):
        return str(self._cfg)

    def __len__(self):
        return len(self._cfg)

    def __iter__(self):
        return iter(self._cfg)

    def locals(self):
        return locals()

    def save(self, fn):
        with open(fn, "w") as file:
            yaml.dump(self._cfg, file)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path: str):
        exists = True
        try:
            self._cfg
        except:
            exists = False

        if Path(path) == self._path:
            print("HARMLESS: Config all ready defined.")
            return

        if exists:
            raise Exception("Config.path(): path variable all ready defined.")

        self._path = Path(path)
        with open(self._path) as f:
            self._cfg: Dict[str, Any] = yaml.load(f, Loader=yaml.FullLoader)

    def append(self, cfg2: Dict[str, Any]):
        """Append another dictionary to our config file."""
        self._cfg.update(cfg2)
