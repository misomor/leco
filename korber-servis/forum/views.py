
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Document, Post, Comment
from .forms import PostModelForm, CommentModelForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@login_required
def category_documents(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    documents = Document.objects.filter(pdfFile=category)
    print(documents)

    qs = Post.objects.filter(category=category_id)
    
    # initials
    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False

    profile = User.objects.get(username=request.user.username)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = PostModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.category = category
            instance.save()
            p_form = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()

    content = {
        'accFiles': documents,
        'qs': qs,
        'profile': profile,
        'p_form': p_form,
        'c_form': c_form,
        'post_added': post_added,
    }
    return render(request,'blank.html',content)

@user_passes_test(lambda u: u.is_staff)
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Zamijenite 'desired_redirect_url' sa željenim URL-om za preusmjeravanje
    else:
        form = CategoryForm(initial={'parent': None, 'name':''})
    return render(request, 'create_category.html', {'form': form})
