from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Student
from .forms import AddStudentForm

# def base(request):
#     return render(request, 'new_app/base.html')


# def home(request):
#     return render(request, 'new_app/home.html')


def get(request):
    std = Student.objects.all()
    return render(request, 'new_app/base.html',{'std':std})


def add(request):
    fm = AddStudentForm(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
        return render(request, 'new_app/add.html', {'fm':fm})

# def edit(request,id):
#     std = Student.objects.get(id=id)
#     fm = AddStudentForm(request.POST, instance=std)
#     if fm.is_valid():
#         fm.save()
#         return redirect('/')
#     else:
#         return render(request, 'new_app/edit.html', {'fm':fm})

def edit(request, id):
    std = Student.objects.get(id=id)
    if request.method == 'POST':
        fm = AddStudentForm(request.POST, instance=std)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = AddStudentForm(instance=std)
    return render(request, 'new_app/edit.html', {'fm': fm})


def delete(request):
    data = request.POST
    id = data.get('id')
    studata = Student.objects.get(id=id)
    studata.delete()
    return redirect('/')

