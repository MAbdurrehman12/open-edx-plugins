"""
ol_openedx_rapid_response Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs, PluginContexts, PluginSettings

from openedx.core.constants import COURSE_ID_PATTERN
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType
from ol_openedx_rapid_response.constants import INCTRUCTOR_DASHBOARD_PLUGIN_VIEW_NAME


class RapidResponsePluginConfig(AppConfig):
    """
    Configuration for the ol_openedx_rapid_response Django application.
    """

    name = 'ol_openedx_rapid_response'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: '',
                PluginURLs.REGEX: 'courses/{}/instructor/api/'.format(COURSE_ID_PATTERN),
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: 'settings.production'},
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        },
        PluginContexts.CONFIG: {
            ProjectType.LMS: {
                INCTRUCTOR_DASHBOARD_PLUGIN_VIEW_NAME: 'ol_openedx_rapid_response.context_api.plugin_context'
            }
        }
    }
