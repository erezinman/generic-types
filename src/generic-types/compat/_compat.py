import sys

# The generics-system was reworked in version 3.7
OLD_GENERICS = sys.version_info[:3] < (3, 7, 0)

if OLD_GENERICS:
    from typing import GenericMeta, TypingMeta, Generic
else:
    GenericMeta = TypingMeta = type
    Generic = object
