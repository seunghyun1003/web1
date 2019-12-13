from django.urls import path
from simp_web import views
from simp_web.views import CreatememoView, MemolistView, MemodetailView, UpdatememoView, DeletememoView

urlpatterns = [
    path("", views.index, name='index'),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreateView.as_view(), name="post_create"),
    path('page', views.page, name='page'),
    path('memo', views.memo, name='memo'),
    path('memo/create', CreatememoView.as_view(), name='add'),
    path('memo/memolist', MemolistView.as_view(), name='memolist'),
    path('memolist/detail/<int:pk>', MemodetailView.as_view(), name='detail'),
    path('memolist/update/<int:pk>', UpdatememoView.as_view(), name='update'),
    path('memolist/delete/<int:pk>', DeletememoView.as_view(), name='delete'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout, name='logout'),
    path('account', views.account, name='account'),
]
