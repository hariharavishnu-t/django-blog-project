from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.db.models import Q

# Create your views here.
# static demo data for posts
#posts = [
#        {'id': 1, 'title': 'Post 1', 'content': 'This is the content of post 1.'},
#        {'id': 2, 'title': 'Post 2', 'content': 'This is the content of post 2.'},
#        {'id': 3, 'title': 'Post 3', 'content': 'This is the content of post 3.'},
#        {'id': 4, 'title': 'Post 4', 'content': 'This is the content of post 4.'},
#    ]


def index(request):
    blog_title = "Latest Posts"

    search_query = request.GET.get('q', '').strip()

    all_posts = post.objects.all()

    if search_query:
        all_posts = all_posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/index.html',
        {
            'blog_title': blog_title,
            'page_obj': page_obj,
            'search_query': search_query,
        }
    )


def detail(request , slug):   
    # static data
    #post = next((item for item in posts if item["id"] == int (post_id)), None)
   
    try:

        #getting data from model by post_id
        selected_post = post.objects.get(slug=slug)
        related_post = post.objects.filter(category=selected_post.category).exclude(pk=selected_post.id)

    except post.DoesNotExist:
        raise Http404("Post does not exist")
 
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')=
    return render(request , 'blog/detail.html',{'post': selected_post, 'related_post': related_post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_views(request):
    return HttpResponse("This is the new URL view.")  

def contact_view(request):
    logger = logging.getLogger("TESTING")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        if form.is_valid():
            
            logger.debug(f'POST data is {form.cleaned_data["name"]}{form.cleaned_data["email"]}{form.cleaned_data["message"]}')
            success_message = "Your Email has been sent successfully!"
            return render(request , 'blog/contact.html', {'form': form, 'success_message': success_message, 'name': name, 'email': email, 'message': message})
        else:
            logger.debug('Form validation failed')
        return render(request , 'blog/contact.html', {'form': form, 'name': name, 'email': email, 'message': message})
    else:
        form = ContactForm()
    return render(request , 'blog/contact.html', {'form': form})

def about_View(request):
    about_content = AboutUs.objects.first().content
    return render(request , 'blog/about.html',{'about_content':about_content})