from typing import Iterator, Tuple

from .compat import OLD_GENERICS, TypeOrAlias


def get_generic_mro():
    pass


def iterate_generic_mro():
    pass


def is_generic(tp: type):
    return is_generic_declaration(tp) or is_generic_specification(tp)


def is_generic_specification(tp: TypeOrAlias):
    pass


def is_generic_declaration(tp: TypeOrAlias):
    pass


def _is_typing_declared_class(tp: TypeOrAlias):
    return tp.__module__ == 'typing'


def _get_description_class(tp: TypeOrAlias) -> type:
    origin = getattr(tp, '__origin__', None)

    if origin is None:
        return tp

    if OLD_GENERICS:
        pass


    if (not OLD_GENERICS) and _is_typing_declared_class(tp):
        if (origin is not None) and (not _is_typing_declared_class()):
            pass


def _get_generic_parameters(tp: TypeOrAlias) -> Iterator:
    """
    Return all "unfilled" generic arguments
    """
    return getattr(tp, '__parameters__', ())


def _get_generic_specifications(tp: type) -> Tuple:
    """
    Return all "filled" generic arguments
    """
    return getattr(tp, '__args__', ())


def get_generic_parameter_assignments(tp: type):
    if OLD_GENERICS:
        pass
    else:
        if not is_generic(tp):
            return
        return tp


def get_non_generic_type(tp: type) -> type:
    pass


def get_generic_parent():
    pass



"""__origin__
__orig_bases__
__bases__
__next_in_mro__
__parameters__"""

"""
__args__
__mro_entries__
__origin__
__parameters__
_special
_inst
_name
"""