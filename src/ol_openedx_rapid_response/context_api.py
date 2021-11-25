from django.utils.translation import ugettext as _
from rapid_response_xblock.utils import get_run_data_for_course


def plugin_context(context):
    """ Provide data for the rapid responses dashboard section """
    course_key = context["course_key"]

    # section_key is the name of html file in templates
    # if section_key is changed then also change the name of html file 

    rapid_response_context = {
        'section_key': 'rapid_response',
        'section_display_name': _('Rapid Responses'),
        'problem_runs': get_run_data_for_course(course_key=course_key),
        'course_key': course_key,
        'download_url': 'get_rapid_response_report'
    }
    context["sections"].append(rapid_response_context)

    return context
