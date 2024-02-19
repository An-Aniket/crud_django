from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Student
from .forms import AddStudentForm
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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


@api_view(['GET', 'POST'])
def display(request):
    if request.method == 'GET':
        std = Student.objects.all()
        serializer = StudentSerializers(std, many= True)
        return Response({"Students":serializer.data})

    
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def api_details(request, id):
    try:
        std = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializers(std)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = StudentSerializers(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        std.delete()
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)