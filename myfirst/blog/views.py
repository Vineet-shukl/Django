from django.shortcuts import render,redirect,get_object_or_404 
from .forms import PostForm
from django.http import HttpResponse
from blog.models import Posts
from .models import Post # Make sure Post is imported
from .forms import PostForm
def blog_index(request):
    return render(request=request, template_name="blog_index.html")
def get_post(request):
    all_posts = Posts.objects.all()
    return render(request=request,template_name='posts.html',context={'posts':all_posts})
def create_post(request):
    print("Test",dir(request))
    title=request.POST.get('title')
    content=request.POST.get('content')
    return render(request=request, template_name='new_post.html')
def home(request):
    posts = Post.objects.all().order_by('-created_at') # Get all posts, newest first
    return render(request, 'home.html', {'posts': posts})
# Create your views here.
def content_post(request):
    # If the form is being submitted (a POST request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        # Check if the submitted data is valid
        if form.is_valid():
            form.save() # Save the new Post object to the database
            return redirect('home') # Redirect to a success page or the homepage
    # If it's a GET request (just loading the page)
    else:
        form = PostForm() # Create a new, blank form instance

    # Render the template with the form
    return render(request, 'new_post.html', {'form': form})




def post_update(request, pk):
    """
    View to handle editing an existing post.
    """
    post = get_object_or_404(Post, pk=pk) # Get the specific post or show a 404 error
    if request.method == 'POST':
        # Populate the form with submitted data AND the existing post instance
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirect to the homepage after saving
    else:
        # Populate the form with the existing post's data
        form = PostForm(instance=post)
    
    # Pass the form to a template
    return render(request, 'blog/post_update.html', {'form': form})


def post_delete(request, pk):
    """
    View to handle deleting a post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST': # Only process if the form was submitted
        post.delete()
        return redirect('home')
    # If it's a GET request, you might show a confirmation page,
    # but we'll handle confirmation in the template for simplicity.
    return redirect('home') # Or render a confirmation template