from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("영화 목록 페이지 입니다.")

def detailview(request):
    return HttpResponse("영화 상세 페이지 입니다.")

def createview(request):
    return HttpResponse("영화 등록 페이지 입니다.")

def modifyview(request):
    return HttpResponse("영화 수정 페이지 입니다.")

def delete(request):
    return HttpResponse("영화 삭제 입니다.(링크)")
