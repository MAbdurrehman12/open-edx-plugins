from django.utils.translation import ugettext as _
from rapid_response_xblock.utils import get_run_data_for_course
from opaque_keys.edx.keys import CourseKey


def plugin_context(context):
    """ 
    Provide data for the rapid responses dashboard section
    section_key in canvas_intgeration_context is the name of html file in templates
    if section_key is changed then also change the name of html file  
    """
    
    course = context.get("course", False)
    sections = context.get("sections", False)
    
    if not (course and sections):
        return None
    
    course_key = course.id

    rapid_response_context = {
        'section_key': 'rapid_response',
        'section_display_name': _('Rapid Responses'),
        'problem_runs': get_run_data_for_course(course_key=course_key),
        'course_key': course_key,
        'download_url': 'get_rapid_response_report',
        'template_path_prefix': '/'
    }
    
    sections.append(rapid_response_context)
    context["sections"] = sections

    return context
