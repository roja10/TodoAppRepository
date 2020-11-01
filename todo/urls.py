from django.conf.urls import url,re_path
from todo import views


urlpatterns = [
    # todo/
    # todo/<pk>
    url('todo/$',views.TodoCreateListView.as_view()),
    re_path(r'todo/(?P<id>[0-9]+)', views.TodoUpdateDeleteView.as_view()),
]
