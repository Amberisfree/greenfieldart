from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name='archive'
urlpatterns = [
    path('', TemplateView.as_view(template_name='archive/main_menu.html'), name='main'),

    #path('oilpainting/', TemplateView.as_view(template_name='archive/main_menu.html'), name='oilpainting'),

    path('oilpainting/', views.PicListView.as_view(), name='oilpainting'),
    path('oilpainting/pic/<int:pk>', views.PicDetailView.as_view(), name='pic_detail'),
    path('oilpainting/pic/create',
         views.PicCreateView.as_view(success_url=reverse_lazy('archive:oilpainting')), name='pic_create'),
    path('oilpainting/pic/<int:pk>/update',
         views.PicUpdateView.as_view(success_url=reverse_lazy('archive:oilpainting')), name='pic_update'),
    path('oilpainting/pic/<int:pk>/delete',
         views.PicDeleteView.as_view(success_url=reverse_lazy('archive:oilpainting')), name='pic_delete'),

    path('oilpainting/pic_picture/<int:pk>', views.stream_file, name='pic_picture'), #actual url to serve the image
    #url generating the html and picture




    path('bookart/', TemplateView.as_view(template_name='archive/main_menu.html'), name='bookart'),
    path('landscapepainting/', TemplateView.as_view(template_name='archive/main_menu.html'), name='landscapepainting'),
    path('watercolor/', TemplateView.as_view(template_name='archive/main_menu.html'), name='watercolor'),
    path('figuredrawing/', TemplateView.as_view(template_name='archive/main_menu.html'), name='figuredrawing'),
]
