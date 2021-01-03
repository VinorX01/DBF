# DBF (Data Bank File)

## About

Open source code. Free to edit and use on projects with or without to profit.

It's is the DBF (Data Bank File) module. A module that allows you create, write and read a .dba and .dbu file.
The .dba and .dbu are a new extensions intentional, created to separate files and reduce read problems, but no are exclusive for this module.

**DBA (Attribute Data Bank)**, the content is a dictionary.

**DBU (Unitary Data Bank)**, the content is a simple key-value object.

## How to use it?

All functions on module returns a list or dictionary with changes makes, look below. 

### For the `dba()` class

The content of file is returned from requisitions as list of values saved in the specified index.

It class manipulate data in dictionary format constituted of infinity attributes for each key on another dictionary. Example that will be used here: `{'example': {'attribute_key': 'attribute_value'}}`, a data named `example` with one attribute in a file '**test.dba**'.

and can be access using index. Ex.: `example[index_on_list]`. The optional system to get values from keys, is a key verification for the each index into the list using for example, a loop `for` or `while`.

#### Functions

`open(name)` open a file.dba with a `name` specified. Creating a file if don't exist.

`save(name, data)` save `data` into the file with `name`. If a data key has saved, it will be replace to new data.

`remove(name, data)` remove `data` into the file with `name`. If a data key has saved, it will be removed.

```
import dbf 

# Create a .dba file named 'test'
data = dbf.dba.open('test')

# Save data 'example' from 'test.dba'
data = dbf.dba.save('test', {'example': {'attribute_key': 'attribute_value'}})

# Remove data 'example' from 'test.dba'
data = dbf.dba.remove('test', {'example': {'attribute_key': 'attribute_value'}})

print(data)
```
OUTPUT
```
[]
```

### For the `dbu()` class
  
The content of file is returned from requisitions as dictionary of values saved in the specified key
and can be access using id. Ex.: `example[id_on_dict]`. Commonly, this method save one content for each key.

It class manipulate data in dictionary format constituted of infinity attributes for each key on another dictionary. Example that will be used here: `{'example': {'attribute_key': 'attribute_value'}}`, a data named `example` with one attribute in a file '**test.dba**'.

and can be access using index. Ex.: `example[index_on_list]`. The optional system to get values from keys, is a key verification for the each index into the list using for example, a loop `for` or `while`.

#### Functions

`open(name)` open a file.dba with a `name` specified. Creating a file if don't exist.

`save(name, data)` save `data` into the file with `name`. If a data key has saved, it will be replace to new data.

`remove(name, data)` remove `data` into the file with `name`. If a data key has saved, it will be removed.

```
import dbf 

# Create a .dba file named 'test'
data = dbf.dba.open('test')

# Save data 'example' from 'test.dba'
data = dbf.dba.save('test', {'example': {'attribute_key': 'attribute_value'}})

# Remove data 'example' from 'test.dba'
data = dbf.dba.remove('test', {'example': {'attribute_key': 'attribute_value'}})

print(data)
```
OUTPUT
```
[]
```