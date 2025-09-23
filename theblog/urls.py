from django.urls import path
from .import views 
from .views import AddCategoryView,homeView,DeletePostView,DetailView,UpdatePostView,AddpostView,CategoryView,categoryListView,LikeView,AddCommentView
urlpatterns = [
    # path('',views.home,name="home"),
    path('',homeView.as_view(),name="home"),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_posts'),
    path('category-list/', views.categoryListView, name='category-list'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/<int:pk>',DetailView.as_view(),name="article_detail"),
    path('add_post/',AddpostView.as_view(),name="add_post"),
    # path('update_post/',UpdatePostView.as_view(),name="update_post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name="add_comment"),




]