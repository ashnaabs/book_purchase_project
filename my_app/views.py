from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AuthorForm,BookForm

# Create your views here.

from .models import Book

# def Createbook(request):
#     if request.method=='POST':
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#
#         book=Book(title=title,price=price)
#         book.save()
#
#     return render(request,'book.html')

def listbook(request):
    books=Book.objects.all()
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'admin/listbook.html',{'books':books,'page':page})

def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book':book})

def updatebook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()

            return redirect('listview')
    else:
        form=BookForm(instance=book)

    return render(request,'admin/updateview.html',{'form':form})

def deletebook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('listview')

    return render(request,'admin/deleteview.html',{'book':book})

def Createbook(request):
    books=Book.objects.all()
    if request.method=='POST':
        form=BookForm(request.POST,files=request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listview')
    else:
        form=BookForm()

    return render(request,'admin/book.html',{'form':form,'books':books})



def CreateAuthor(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('listview')
    else:

        form=AuthorForm()

    return render(request,'admin/author.html',{'form':form})

def index(request):
    return render(request,'admin/base.html')

def Searchbook(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]
    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)


