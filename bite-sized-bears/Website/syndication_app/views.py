from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Post, Comments, User

def index(request):
    return HttpResponse("Hello, world. You're at the Syndication index.")


class IndexListView(ListView):
    paginate_by = 25
    template_name = "index.html"
    queryset = Post.objects.all()

def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponse('<h1>Post does not exist</h1>')

    comments = Comments.objects.filter(post=post).order_by('creation_date')
    return render(request, 'post_template.html', {'post':post, 'comments':comments})

def comment_add(request, post_id):
    if not 'content' in request.POST.keys():
        return HttpResponse('<h1>404 error lol</h1>')#change
    try:
        user = User.objects.get(id=1)#change
    except:
        return HttpResponse('<h1>You must be logged in to add comments</h1>')
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponse('<h1>The post you are searching for doesnt exist</h1>')
    Comments.objects.create(content=request.POST['content'], author=user, post=post)

    return HttpResponseRedirect(f'/posts/{post.id}')
