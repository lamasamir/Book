from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,User_Data
from django.http import JsonResponse,HttpResponse
from .forms import style_bookform,UserForm,SearchForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone



# Create your views here.




def homepage(request):  
        book = Book.objects.all()
        return render(request,"book/bookworld.html",{"books":book})
    
def create_post(request):    
    if request.method == "GET":
       return render(request,"book/bookworld.html",{"book":style_bookform})
    elif request.method == "POST": 
        book =style_bookform(request.POST)
        if book.is_valid():
            notification = "Bokk is saved !!"
            messages.success(request,notification)
            book.save()
            return redirect("homepage")
        else:    
            notification = "Book is not saved!!"
            messages.error(request,notification)
            return redirect("homepage")


def contact(request):
    return render(request,"book/contact.html")

def privacy_policy(request):
    return render(request,"book/privacy.html")

def terms(request):
    return render(request,"book/terms.html")


def login_user(request):
    if request.method == 'POST':
       username = request.POST ['username']
       password = request.POST ['password']
       user = authenticate(request,username=username,password=password)
       if user is not None:
        login(request,user)
        messages.success(request,"you have login successfully!!")
        return redirect("homepage")
       else:
        messages.error(request,"there is error on you login,plesase try again")
        return redirect("login")
    
    else:
        form = AuthenticationForm()

    return render(request, 'book/login.html', {'form': form, 'hide_footer': True})


def logout_user(request):
    logout(request)
    return redirect("homepage")

def signin(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'book/signin.html', {'form': form, 'hide_footer': True})

def search_books(request):
    form = SearchForm(request.GET)  # Use GET to retrieve search query from URL
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            books = books.filter(title__icontains=query) | books.filter(author__icontains=query) | books.filter(genre__icontains=query)

    return render(request, 'book/browse.html', {'form': form, 'books': books})   


def new_books(request):
    books = Book.objects.all().order_by('-uploaded_at')[:10]  # latest 10 books
    return render(request, 'book/newbook.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/book_detail.html', {'book': book})  

# def Insert_Data(request):
#     if request.method == "GET":
#         user = UserForm()
#         context = {"user":user}
#         return render(request,'book/userForm.html',context)
#     elif request.method == "POST":
#         user = UserForm(request.POST)
#         user_context = {"user":user}
#         if user.is_valid():
#             user.save()
#             return HttpResponse("data is saved!!")
#         else:
#             return render(request,"book/userForm.html",user_context)

def is_admin_or_staff(user):
     return user.is_authenticated and (user.is_staff or user.is_superuser)
@user_passes_test(is_admin_or_staff)
def insert_book(request):   
    if request.method == "GET":
        form = style_bookform()
        return render(request, 'book/insertbook.html', {"form": form})
    elif request.method == 'POST':
        form = style_bookform(request.POST, request.FILES)
        if form.is_valid():
         form.save()
         return redirect('homepage')
        else:
         form = style_bookform()

         return render(request, 'book/insertbook.html', {
        'form': form,
        'editing': False,
    })
@user_passes_test(is_admin_or_staff)
def edit_book(request, id):
    book_instance = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = style_bookform(request.POST, request.FILES, instance=book_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("homepage")
        else:
            messages.error(request, "Failed to update book.")
    else:
        form = style_bookform(instance=book_instance)

    
    return render(request, "book/insertbook.html", {
        "form": form,
        "book": book_instance,
        "editing": True,
        "editing_id": id
    })

@user_passes_test(is_admin_or_staff)
def delete_book(request, id):
    book_to_delete = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book_to_delete.delete()
        messages.success(request, "Book has been deleted successfully.")
        return redirect("homepage")

    return redirect("homepage")


         
         





