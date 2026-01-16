
from blogs.models import Category , Blog
from assignment.models import FollowUs


def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_FollowUs(request):
    follow_us=FollowUs.objects.all()
    return dict(follow_us=follow_us)
 
def get_Blog(request):
    blog_ele=Blog.objects.all() 
    return dict(blog_ele=blog_ele)