# (Vaguely based on pyramid_jinja2 code)

from paste.util.template import paste_script_template_renderer
try:
    from pyramid.scaffolds import PyramidTemplate # pyramid 1.1+
except ImportError: # pragma: no cover
    from pyramid.paster import PyramidTemplate # pyramid 1.0


class DecoupledProjectTemplate(PyramidTemplate):
    _template_dir = 'decoupled_project_template'
    summary = 'Decouple web-specific code from the rest (models, library api, etc).'
    template_renderer = staticmethod(paste_script_template_renderer)
