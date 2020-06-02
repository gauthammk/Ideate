from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IdeaCreateForm, IdeaUpdateForm
from django.contrib import messages
from .models import Idea, Tag
from django.core.exceptions import PermissionDenied


def index(request):
    context = {'title': 'Index'}
    return render(request, 'ideas/index.html', context)


@login_required
def tagHome(request, pk):
    try:
        selectedTag = Tag.objects.get(id=pk)
        ideas = Idea.objects.filter(tags=selectedTag)
        context = {'tag': selectedTag,
                   'ideas': ideas,
                   'title': '#' + selectedTag.name,
                   }
        return render(request, 'ideas/tag_home.html', context)
    except Exception:
        return render(request, 'ideas/error.html', {'error': 'The requested page could not be found.'})
    finally:
        selectedTag = None


def error(request):
    return render(request, 'ideas/error.html')


@login_required
def home(request):
    try:
        user = request.user
        tags = Tag.objects.all()
        context = {
            'title': 'Home',
            'user': user,
            'tags': tags,
        }
        return render(request, 'ideas/home.html', context)
    except Exception:
        return render(request, 'ideas/error.html', {'error': 'The requested page could not be found.'})
    finally:
        user = None


@login_required
def ideaCreate(request):
    if request.method == 'POST':
        form = IdeaCreateForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Your idea has been created!')
            return redirect('idea-list')
    else:
        form = IdeaCreateForm()
    return render(request, 'ideas/idea_create.html', {'form': form,
                                                      'title': 'Create Idea'})


@login_required
def ideaList(request):
    try:
        ideas = Idea.objects.filter(author=request.user)
        context = {'ideas': ideas, 'title': 'My Ideas'}
        return render(request, 'ideas/idea_list.html', context)
    except Exception:
        return render(request, 'ideas/error.html', {'error': 'The requested page could not be found.'})
    finally:
        ideas = None


@login_required
def ideaUpdate(request, pk):
    try:
        idea = Idea.objects.get(id=pk, author=request.user)
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
    except Exception:
        return render(request, 'ideas/error.html', {'error': 'The requested action could not be performed.'})
    finally:
        idea = None


@login_required
def ideaDelete(request, pk):
    try:
        idea = Idea.objects.get(id=pk)
        print('deleting idea : ', idea)
        idea.delete()
        messages.success(request, f'Your idea has been deleted!')
        return redirect('idea-list')
    except Exception:
        return render(request, 'ideas/error.html', {'error': 'The requested action could not be performed.'})
    finally:
        idea = None
