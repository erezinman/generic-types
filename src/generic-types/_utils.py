from .compat import OLD_GENERICS


def get_generic_mro():
    pass


def iterate_generic_mro():
    pass


def is_generic(tp: type):
    pass


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