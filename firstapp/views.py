from django.shortcuts import render
from .models import *
from .forms import UserForm
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404


userform = UserForm()


def null(request):
    context = {
              'posts': Post.objects.all().order_by('-last_pub_date'),
              'form': userform
    }
    return render(request, "null.html", context)

def thread(request,id):
        context = {
                  'post': Post.objects.get(id=id),
                  'form': userform
        }
        return render(request, "thread.html", context)



def create(request):
     if request.method == "POST":
        tom = Post()
        tom.name_d = request.POST.get("name")
        tom.text_d = request.POST.get("text")
        tom.image_d = request.FILES.get("image")
        tom.pub_date = datetime.datetime.now()
        tom.last_pub_date = datetime.datetime.now()
        tom.save()
        return HttpResponseRedirect("/null")

def create_comment(request,pk):
    if request.method == "POST":
       tom = Comment()
       tom.name_d = request.POST.get("name")
       tom.text_d = request.POST.get("text")
       tom.image_d = request.FILES.get("image")
       tom.pub_date = datetime.datetime.now()
       tom.last_pub_date = datetime.datetime.now()
       post =get_object_or_404(Post, pk=pk)
       post.last_pub_date = datetime.datetime.now()
       post.save()
       tom.post = post
       tom.save()
       response = "/thread/{}".format(pk)
       return HttpResponseRedirect(response)
