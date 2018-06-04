from django.conf.urls import url,include

from app01.views import *


urlpatterns = [
    # 方式一
    # url(r'^course/$', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    # 方式二
    url(r'^course/$', CourseView.as_view({'get':'list'})),

    url(r'^course/(?P<pk>\d+)/$',CourseView.as_view({'get':'retrieve'})),

    url(r'^oftenAskedQuestion/$', OftenAskedQuestionView.as_view({'get':'list'})),
    url(r'^courseChapter/$', CourseChapterView.as_view({'get':'list'})),
    url(r'^article/$', ArticleView.as_view({'get':'list'})),
    url(r'^comment/$', CommentView.as_view({'get':'list'})),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view({'get':'retrieve'})),

]
