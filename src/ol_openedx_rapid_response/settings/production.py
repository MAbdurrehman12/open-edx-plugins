"""Production settings unique to the rapid response plugin."""

from path import Path as path

def _update_template_dirs(template_engines):
    PLUGIN_ROOT = path(__file__).abspath().dirname().dirname()
    for engine in template_engines:
        template_dirs = engine['DIRS']
        template_dirs.append(
            PLUGIN_ROOT + '/templates',
        )
        engine['DIRS'] = template_dirs
    return template_engines

def plugin_settings(settings):
    settings.TEMPLATES = _update_template_dirs(settings.TEMPLATES)