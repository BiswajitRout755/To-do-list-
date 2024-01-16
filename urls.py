from django.urls import path
from django.urls import reverse_lazy
 #importing every page routes being structured in the function format inside views.py....
from .views import TaskList,TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, logout_view,RegisterPage



#urlpatterns contains every routing page details..like: architecture of the address paths, function in views.py, name of the page
urlpatterns =[
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view , name='logout'),
    path('register/', RegisterPage.as_view() , name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/' , TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]