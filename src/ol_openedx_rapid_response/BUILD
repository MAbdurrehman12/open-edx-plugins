python_library(
    name="rapid_response_plugin_dependencies",
)

resources(
  name="rapid_reponse_plugin_templates",
  sources=[],
  dependencies=["src/ol_openedx_rapid_response/templates:rapid_response_templates"]
)

python_distribution(
    name="rapid_response_plugin_dist",
    dependencies=[":rapid_response_plugin_dependencies", ":rapid_reponse_plugin_templates"],
    provides=setup_py(
        name="ol-openedx-rapid-response",
        version="0.1.0",
        description="An Open edX plugin to add rapid response reports support",
        entry_points={
            "lms.djangoapp": ["ol_openedx_rapid_response = ol_openedx_rapid_response.app:RapidResponsePluginConfig"],
            "cms.djangoapp": []
        }
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
