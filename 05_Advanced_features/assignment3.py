import os

class ConfigDict(dict):

    def __init__(self, filename):

        self._config_file = filename
        assert os.path.isfile(self._config_file), "File not found"
        with open(self._config_file) as fh:
            config_list = [line.rstrip().split('=', 1) for line in fh]
        config_dict = {dict.__setitem__(self, x[0], x[1]) for x in config_list}

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        with open(self._config_file, "a") as fh:
            fh.write("%s=%s\n" % (key, val))
