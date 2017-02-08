# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Student
from models import Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


# students views

def students_list(request):
    students = Student.objects.all()
    # Defining students list ordering
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
        students = students.reverse()

    # Students list pagination
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return the first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range.
        # return last page with results
        students = paginator.page(paginator.num_pages)
    return render(request, 'students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Add students</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)


# groups views

def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Add group</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete group %s</h1>' % gid)

def test(request):
    from studentsdb.settings import MEDIA_ROOT
    full_path = MEDIA_ROOT + request.path
    return HttpResponse('<h1> You request path is: "<a href="#">%s</a>"</h1>'
                        % full_path)
# attendance views
def attendance(request):
    students = (
        {'id': 1,
         'first_name': 'Kimmi',
         'last_name': 'Raikkonen'},
        {'id': 2,
         'first_name': 'Sebastian',
         'last_name': 'Vettel'},
        {'id': 3,
         'first_name': 'Nico',
         'last_name': 'Rosberg'},
    )

    return render(request, 'attendance.html', {'students': students})
