python_library(
    name="canvas_integration",
    dependencies=["src/ol_openedx_canvas_integration/settings:canvas_settings"]
)

python_distribution(
    name="canvas_integration_package",
    dependencies=[":canvas_integration"],
    provides=setup_py(
        name="ol-openedx-canvas-integration",
        version="0.1.0",
        description="An Open edX plugin to add canvas integration support",
        entry_points={
            "lms.djangoapp": ["ol_openedx_canvas_integration = ol_openedx_canvas_integration.app:CanvasIntegrationConfig"],
            "cms.djangoapp": []
        }
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
