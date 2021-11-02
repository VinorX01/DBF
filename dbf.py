"""
Open source code. Free to edit and use on projects with or without to profit.

It's is the DBF (Data Bank File) module. A module that allows you create, write and read a .dba and .dbu file.
The .dba and .dbu are a new extensions intentional created to separate files and reduce read problems, but no are exclusive for this module.

For the "dba()" class:
The content of file is returned from requisitions as list of values saved in the specified index
and can be access using index. Ex.: example[index_on_list]. The optional system to get values from keys, is a key verification for the each index into the list using for example, a loop 'for' or 'while'.

For the "dbu()" class:
The content of file is returned from requisitions as dictionary of values saved in the specified key
and can be access using id. Ex.: example[key_on_dict]. Commonly, this method save one content for each key.

The documentation is available on GitHub repository README.md

by Valdivino Junior (VinorX01)
Github repository: https://github.com/VinorX01/DBF
"""

# The 'dba' class begins

class dba():

    # Index the data of file.dba
    def index(self):
        data = self
        data = data.split('/')
        data_indexed = []

        try:
            for index in range(0, len(data) - 1):
                format01 = data[index].split('|')
                format02 = format01[1].split('#')
                dic = {}
                for index02 in range(0, len(format02) - 1):
                    format03 = format02[index02].split(';')
                    dic.update({format03[0]: format03[1]})
                data_indexed.append({format01[0]: dic})

        except:
            data_indexed = '[ERROR!] Failed to index the data'
            if len(data) == 0:
                data_indexed = '[ATTENTION!] No data found'

        return data_indexed

    # Compile the entry data
    def compile(self):
        try:
            data = self
            keys = list(data.keys())[0]
            values = list(data[keys].values())
            data_compiled = keys + '|'
            keys = list(data[keys])

            for index in range(0, len(keys)):
                data_compiled += str(keys[index]) + ';' + str(values[index]) + '#'
            data_compiled += '/'

        except:
            data_compiled = '[ERROR!] Failed to compile the data'
            if len(data) == 0:
                data_compiled = '[ATTENTION!] No data found'

        return data_compiled

    # Open the data bank file.dba
    def open(self):
        try:
            try:
                open(f'{self}.dba', 'x')
                databank = open(f'{self}.dba', 'r')

            except:
                databank = open(f'{self}.dba', 'r')

            data_indexed = dba.index(databank.read())
            databank.close()

        except:
            data_indexed = []

        return data_indexed

    # Save a data on file.dba
    def save(self, data):
        data_compiled = dba.compile(data)
        count = 0
        text = ''
        if data_compiled != '[ERROR!] Failed to compile the data' and data_compiled != '[ATTENTION!] No data found':
            databank = open(f'{self}.dba', 'r')
            data_indexed = dba.index(databank.read())
            for index in range(0, len(data_indexed)):
                if list(data.keys())[0] == list(data_indexed[index].keys())[0]:
                    text += dba.compile(data)
                    count += 1
                else:
                    text += dba.compile(data_indexed[index])

            if count == 0:
                text += dba.compile(data)
            databank = open(f'{self}.dba', 'w')
            databank.write(text)
            databank = open(f'{self}.dba', 'r')
            data_indexed = dba.index(databank.read())
        databank.close()

        return data_indexed

    # Remove a data on file.dba
    def remove(self, key):
        bank = open(f'{self}.dba', 'r')
        databank = dba.index(bank.read())
        for index in range(0, len(databank)):
            if key == list(databank[index].keys())[0]:
                del databank[index]
                break

        try:
            text = ''
            for index02 in range(0, len(databank)):
                text += dba.compile(databank[index02])
            bank = open(f'{self}.dba', 'w')
            bank.write(text)
            bank = open(f'{self}.dba', 'r')
            data_indexed = dba.index(bank.read())
            bank.close()

            return data_indexed

        except:
            bank = open(f'{self}.dba', 'w')
            bank.write('')
            bank = open(f'{self}.dba', 'r')
            data_indexed = dba.index(bank.read())
            bank.close()

            return data_indexed

# The 'dbu' class begins

class dbu():

    # Index the data of file.dbu
    def index(self):
        data = self
        data = data.split('/')
        data_indexed = {}

        try:
            for index in range(0, len(data) - 1):
                format01 = data[index].split('|')
                data_indexed.update({format01[0]: format01[1]})

        except:
            data_indexed = '[ERROR!] Failed to index the data'
            if len(data) == 0:
                data_indexed = '[ATTENTION!] No data found'

        return data_indexed

    # Compile the entry data
    def compile(self):
        try:
            data = self
            key = list(data.keys())[0]
            value = data[key]
            data_compiled = key + '|' + value + '/'

        except:
            data_compiled = '[ERROR!] Failed to compile the data'
            if len(data) == 0:
                data_compiled = '[ATTENTION!] No data found'

        return data_compiled

    # Open the data bank file.dbu
    def open(self):
        try:
            try:
                open(f'{self}.dbu', 'x')
                databank = open(f'{self}.dbu', 'r')

            except:
                databank = open(f'{self}.dbu', 'r')
            data_indexed = dbu.index(databank.read())
            databank.close()

        except:
            data_indexed = {}

        return data_indexed

    # Save a data on file.dbu
    def save(self, data):
        data_compiled = dbu.compile(data)
        count = 0
        text = ''
        if data_compiled != '[ERROR!] Failed to compile the data' and data_compiled != '[ATTENTION!] No data found':
            databank = open(f'{self}.dbu', 'r')
            data_indexed = dbu.index(databank.read())
            for index in range(0, len(data_indexed)):
                if list(data.keys())[0] == list(data_indexed.keys())[index]:
                    text += dbu.compile(data)
                    count += 1
                else:
                    key = list(data_indexed.keys())[index]
                    text += dbu.compile({list(data_indexed.keys())[index]: data_indexed[key]})
            if count == 0:
                text += dbu.compile(data)
            databank = open(f'{self}.dbu', 'w')
            databank.write(text)
            databank = open(f'{self}.dbu', 'r')
            data_indexed = dbu.index(databank.read())
            databank.close()

            return data_indexed

    # Remove a data on file.dbu
    def remove(self, key):
        bank = open(f'{self}.dbu', 'r')
        databank = dbu.index(bank.read())
        for index in range(0, len(databank)):
            if key == list(databank.keys())[index]:
                del databank[key]
                break

        try:
            text = ''
            keys = list(databank.keys())
            for index02 in range(0, len(databank)):
                text += dbu.compile({keys[index02]: databank[keys[index02]]})

            bank = open(f'{self}.dbu', 'w')
            bank.write(text)
            bank = open(f'{self}.dbu', 'r')
            data_indexed = dbu.index(bank.read())
            bank.close()

            return data_indexed

        except:
            bank = open(f'{self}.dbu', 'w')
            bank.write('')
            bank = open(f'{self}.dbu', 'r')
            data_indexed = dbu.index(bank.read())
            bank.close()

            return data_indexed
