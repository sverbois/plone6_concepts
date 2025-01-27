from plone import api


def move_field_value(content_type_name, source_field_name, target_field_name):
    brains = api.content.find(portal_type=content_type_name)
    for brain in brains:
        obj = brain.getObject()
        if hasattr(obj, source_field_name):
            setattr(obj, target_field_name, getattr(obj, source_field_name))
            delattr(obj, source_field_name)
