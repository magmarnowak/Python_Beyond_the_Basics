import os

class ConfigKeyError(Exception):
    """
    Custom exception raised when user inputs a nonexsistent key.
    Raises KeyError and retruns a list of exsisting keys.
    """

    def __init__(self, ConfigDict, key):
        self.message = 'Key "{0}" not found. Available keys: ({1})'.format(key, ', '.join(ConfigDict.keys()))

    def __str__(self):
        return self.message

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

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)
