__author__ = 'paul'

from .settings import PORTAL_URL

def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}

def attendance_month(request):
    return {'month': 'February'}
