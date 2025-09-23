from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse



# Create your views here.
# def home(request):
#     return render(request,"home.html",{})


def LikeView(request, pk):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:    
        post.likes.add(request.user)
        liked = True
    return redirect('article_detail', pk=pk)


def categoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,"category_lis.html",{'cat_menu_list':cat_menu_list})


class homeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-posted_at']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(homeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]= cat_menu
        return context
            
        





class DetailView(DetailView):
    model = Post
    template_name = 'details.html'

class AddpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')

    def form_valid(self, form):
        form.instance.author = self.request.user  # <-- secure assignment
        return super().form_valid(form)
    


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'registration/add_comment.html'
    
    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')


class CategoryView(ListView):
    model = Post
    template_name = 'categories.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
    
    
class AddCategoryView(CreateView):
    model = Category
    fields = ['name']   # only show name
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')