
from django.urls import reverse
from django.utils.translation import ugettext as _
from web_fragments.fragment import Fragment
from django.contrib.staticfiles.storage import staticfiles_storage


def plugin_context(context):
    """ 
    Provide data for the canvas dashboard section
    section_key in canvas_intgeration_context is the name of html file in templates
    if section_key is changed then also change the name of html file 
    """

    course = context.get("course", False)
    sections = context.get("sections", False)

    if not (course and sections):
        return None

    fragment = Fragment()
    fragment.add_javascript_url(staticfiles_storage.url('/js/canvas_integration.js'))
    
    canvas_intgeration_context = {
        'section_key': 'canvas_integration',
        'section_display_name': _('Canvas'),
        'course': course,
        'add_canvas_enrollments_url': reverse(
            'add_canvas_enrollments', kwargs={'course_id': course.id}
        ),
        "list_canvas_enrollments_url": reverse("list_canvas_enrollments", kwargs={"course_id": course.id}),
        "list_canvas_assignments_url": reverse("list_canvas_assignments", kwargs={"course_id": course.id}),
        "list_canvas_grades_url": reverse("list_canvas_grades", kwargs={"course_id": course.id}),
        'list_instructor_tasks_url': '{}?include_canvas=true'.format(reverse(
            'list_instructor_tasks',
            kwargs={'course_id': course.id}
        )),
        "push_edx_grades_url": reverse(
            "push_edx_grades", kwargs={"course_id": course.id}
        ),
        "fragment": fragment,
        "template_path_prefix":"/"
    }

    sections.append(canvas_intgeration_context)
    context["sections"] = sections

    return context

    