import sys
from typing import Type, Union

# The generics-system was reworked in version 3.7
OLD_GENERICS = sys.version_info[:3] < (3, 7, 0)

if OLD_GENERICS:
    from typing import GenericMeta, TypingMeta, Generic, Union

    TypeOrAlias = type
else:
    from typing import _GenericAlias
    GenericMeta = TypingMeta = type
    Generic = object

    TypeOrAlias = Union[type, _GenericAlias]

TypeOrAlias = TypeOrAlias