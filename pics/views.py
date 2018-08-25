from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
def index(request):
    latest_post = Post.objects.order_by('-pub_date')[:1]
    template = loader.get_template('pics/index.html')
    context = {
        'latest_post': latest_post,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    #return HttpResponse ("this is the about page")
    return render(request, 'pics/about.html')