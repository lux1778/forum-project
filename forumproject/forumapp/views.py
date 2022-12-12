from django.shortcuts import render, get_object_or_404
from .models import Forum, Comment


# Create your views here.


def post_list(request):
    posts = Forum.objects.all()
    context = {
        'object_list': posts,
    }
    return render(request, 'forum/post_list.html', context)

def post_detail(request, get_slug):
    post = get_object_or_404(Forum, slug=get_slug)

    context = {
        'object': post
    }
    return render(request, 'forum/post_details.html', context)


# def post_comments(request):
#     comm = get_object_or_404(Comment)
#
#     context = {
#         'comment': comm
#     }
#     return render(request, 'forum/post_details.html', context)


from django.shortcuts import render

# Create your views here.
