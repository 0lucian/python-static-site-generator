from genericpath import isdir
from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self._source = Path(source)
        self._dest = Path(source)

    def create_dir(self, path):
        directory = self._dest / Path.relative_to(self._source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self._dest.mkdir(parents=True, exist_ok=True)

        for path in self._source.rglob("*"):
            if path.isdir():
                self.create_dir(path)
