# (Vaguely based on pyramid_jinja2 code)
from pyramid.scaffolds import PyramidTemplate # pyramid 1.1+


class DecoupledProjectTemplate(PyramidTemplate):
    _template_dir = 'decoupled_project_template'
    summary = 'Decouple web-specific code from the rest (models, library api, etc).'
