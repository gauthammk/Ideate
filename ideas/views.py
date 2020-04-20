from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IdeaCreateForm, IdeaUpdateForm
from django.contrib import messages
from .models import Idea, Tag
from django.forms import ValidationError


def index(request):
    context = {'title': 'Index'}
    return render(request, 'ideas/index.html', context)


@login_required
def tagHome(request, pk):
    selectedTag = Tag.objects.get(id=pk)
    ideas = Idea.objects.filter(tags=selectedTag)
    context = {'tag': selectedTag,
               'ideas': ideas,
               }
    return render(request, 'ideas/tag_home.html', context)


def error(request):
    context = {'error': 'Does not exist.'}
    return render(request, 'ideas/error.html', context)


@login_required
def home(request):
    user = request.user
    tags = Tag.objects.all()
    context = {
        'title': 'Home',
        'user': user,
        'tags': tags,
    }
    return render(request, 'ideas/home.html', context)


@login_required
def ideaCreate(request):
    if request.method == 'POST':
        form = IdeaCreateForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Your idea has been created!')
            return redirect('home')
    else:
        form = IdeaCreateForm()
    return render(request, 'ideas/idea_create.html', {'form': form,
                                                      'title': 'Create Idea'})


@login_required
def ideaList(request):
    ideas = Idea.objects.filter(author=request.user)
    context = {'ideas': ideas, 'title': 'My Ideas'}
    return render(request, 'ideas/idea_list.html', context)


@login_required
def ideaUpdate(request, pk):
    idea = Idea.objects.get(id=pk)
    # check if the current user is the author of the idea
    if idea.author != request.user:
        raise ValidationError(
            "Access restricted. You are not the author of the idea.")
    if request.method == 'POST':
        form = IdeaUpdateForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your idea has been updated!')
            return redirect('idea-list')
    else:
        form = IdeaUpdateForm(instance=idea)
    return render(request, 'ideas/idea_update.html', {'form': form,
                                                      'idea': idea,
                                                      'title': 'Update'})


@login_required
def ideaDelete(request, pk):
    idea = Idea.objects.get(id=pk)
    print('deleting idea : ', idea)
    idea.delete()
    messages.success(request, f'Your idea has been deleted!')
    return redirect('idea-list')
