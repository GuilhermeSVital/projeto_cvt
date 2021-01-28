# coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse

def index (request):
    return render(request, 'index.html')

def cursos_list (request):
    return render(request, 'cursos_list.html')

def curso (request):
    return render(request, 'curso.html')

def contato (request):
    return render(request, 'contato.html')
