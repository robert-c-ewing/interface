from .functional import keyfilter



def get_attributes(cls):
    """Gets all attributes from a class."""
    annotations = cls.__annotations__
    defaults = {
        x: getattr(cls, x) for x in dir(cls)
        if '__' not in x
           and not callable(getattr(cls, x))
        }

    return annotations, defaults


def update_clsdict_with_attr_info(clsd: dict) -> dict:
    """Updates the clsdict of a metaclass with attribute information."""
    annotation_key = '__annotations__'
    attr_defaults = {}

    # Note and remove annotations from class dict
    if annotation_key in clsd:
        attr_annots = clsd[annotation_key]
        del clsd['__annotations__']
    else:
        attr_annots = dict()

    for name, value in keyfilter(is_interface_field_name, clsd).items():
        if callable(name):
            continue

        # Use type from annotations, if available
        if name in attr_annots:
            vtype = attr_annots[name]
        else:
            vtype = type(value)

        attr_defaults[name] = (vtype, value)

    clsd['_annotations'] = attr_annots
    clsd['_attr_defaults'] = attr_defaults

    return clsd
