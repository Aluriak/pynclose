"""This script will segfault at the second call,
unless the global variables of the C module can be resetted.

"""

import pynclose as pc

out = pc.concepts('liveinwater.cxt', 1, 1)
print(out)
for obj in out:
    print(obj)

print()
print()
print()

out = pc.concepts('liveinwater.cxt', 1, 1)
print(out)
for obj in out:
    print(obj)
