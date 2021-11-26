#%%
class Aliasor:
    def __init__(self, alias_file):
        import pandas as pd

        aliases = pd.read_json('pango_designation/alias_key.json')

        self.alias_dict = {}
        for column in aliases.columns:
            if column.startswith('X'):
                self.alias_dict[column] = column
            else:
                self.alias_dict[column] = aliases[column][0]

        self.alias_dict['A'] = 'A'
        self.alias_dict['B'] = 'B'

        self.realias_dict = {v: k for k, v in self.alias_dict.items()}

    def compress(self,name):
        name_split = name.split('.')
        if len(name_split) < 5:
            return name
        letter = self.realias_dict[".".join(name_split[0:4])]
        if len(name_split) == 5:
            return letter + '.' + name_split[4]
        else:
            return letter + '.' + ".".join(name_split[4:])

    def uncompress(self,name):
        name_split = name.split('.')
        letter = name_split[0]
        unaliased = self.alias_dict[letter]
        if len(name_split) == 1:
            return name
        if len(name_split) == 2:
            return unaliased + '.' + name_split[1]
        else:
            return unaliased + '.' + ".".join(name_split[1:])
