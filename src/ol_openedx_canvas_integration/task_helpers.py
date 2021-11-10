"""
Helper functions for canvas integration tasks
"""
from time import time

from ol_openedx_canvas_integration import api
from lms.djangoapps.courseware.courses import get_course_by_id
from lms.djangoapps.instructor_task.tasks_helper.runner import TaskProgress


def sync_canvas_enrollments(_xmodule_instance_args, _entry_id, course_id, task_input, action_name):
    """Partial function to sync canvas enrollments"""
    start_time = time()
    num_reports = 1
    task_progress = TaskProgress(action_name, num_reports, start_time)
    api.sync_canvas_enrollments(
        course_key=task_input["course_key"],
        canvas_course_id=task_input["canvas_course_id"],
        unenroll_current=task_input["unenroll_current"],
    )
    # for simplicity, only one task update for now when everything is done
    return task_progress.update_task_state(extra_meta={
        "step": "Done"
    })


def push_edx_grades_to_canvas(_xmodule_instance_args, _entry_id, course_id, task_input, action_name):
    """Partial function to push edX grades to canvas"""
    start_time = time()
    num_reports = 1
    task_progress = TaskProgress(action_name, num_reports, start_time)
    course = get_course_by_id(course_id)
    api.push_edx_grades_to_canvas(
        course=course
    )
    return task_progress.update_task_state(extra_meta={
        "step": "Done"
    })
