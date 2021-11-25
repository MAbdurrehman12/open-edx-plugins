"""Production settings unique to the canvas integration plugin."""

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
    """Settings for the canvas integration plugin."""
    settings.CANVAS_ACCESS_TOKEN = settings.AUTH_TOKENS.get(
        "CANVAS_ACCESS_TOKEN", settings.CANVAS_ACCESS_TOKEN
    )
    settings.CANVAS_BASE_URL = settings.ENV_TOKENS.get(
        "CANVAS_BASE_URL", settings.CANVAS_BASE_URL
    )

    settings.TEMPLATES = _update_template_dirs(settings.TEMPLATES)