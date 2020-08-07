from django.http import HttpResponse
from django.shortcuts import render
from syndication_app.forms import PostForm
from syndication_app.models import Community, User
from django.http import HttpResponseRedirect


def create_post_form(request, community):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        try:
            post.publisher = Community.objects.get(name = community)
        except:
            return HttpResponse('<h1>Community doesn\'t exist</h1>')
        try:
            post.author = User.objects.get(id=1)#change
        except:
            return HttpResponse('<h1>You must be logged in to see posts</h1>')
        post.save()
        return HttpResponseRedirect(f'/posts/{post.id}')

    return render(request, 'create_post_form.html', {'form':form})
