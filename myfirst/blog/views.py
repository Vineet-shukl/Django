from django.shortcuts import render
def blog_index(request):
    return render(request=request, template_name="blog_index.html")
def get_post(request):
    return render(request=request,template_name='posts.html')
# Create your views here.
