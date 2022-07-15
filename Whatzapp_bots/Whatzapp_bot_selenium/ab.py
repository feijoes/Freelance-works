
from os import walk

filenames = next(walk(__file__[:-5]+"errores"), (None, None, []))[2]  # [] if no file
print(filenames)