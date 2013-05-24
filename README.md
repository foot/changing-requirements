changing-requirements
=====================

A kata to spur discussions on refactoring.

We start by implementing a solution to a simple set of requirements. The requirements are modified, the implementation must be changed and we have a chat about it.

1. A CSV query function in python
------------
```python
def query(filename, column_index, value):
    """
    Given the name of a csv file,
    return a list of all the rows where row[column_index] == value.
    """
    pass
```

Proposals for step 2.
 
 - Single CSV -> Multple CSVs
 - CSV -> JSON
 - Exact matching -> Fuzzy matching
 - No time restiction -> Time restriction E.g. 1 sec with a very large file.
 - No memory restriction -> Memory restriction E.g. 10mb with a 100mb file.
 - Matching multiple columns... joins...
