

from rest_framework.views import APIView

from rest_framework.viewsets import GenericViewSet,ViewSetMixin

from app01.models import *

# from app01.serilizer.serilizer import CourseDetailSerializer
from app01.serilizer.serilizer import *

from rest_framework.response import Response

# ViewSetMixin作用是as_view可以传参数
class CourseView(ViewSetMixin,APIView,):


    def list(self,request,*args,**kwargs):

        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret={'code':1000,'data':None}
        try:
            queryset = Course.objects.all()


            # instance指定序列化的对象

            ser = CourseSerializer(instance=queryset,many=True)

            ret['data']=ser.data
        except Exception as e:


            ret['code']=1001
            ret['error']='获取课程失败'
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):

        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        ret={'code':1000,'data':None}

        try:
            # 课程id=2

            pk = kwargs.get('pk')

            # 课程详细对象
            obj = CourseDetail.objects.filter(course_id=pk).first()
            # print(obj)

            ser = CourseDetailSerializer(instance=obj,many=False)

            ret['data']=ser.data
            print(ser.data)
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        # print(ret)
        return Response(ret)


class OftenAskedQuestionView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):

        ret = {'code': 1000, 'data': None}
        try:

            queryset = OftenAskedQuestion.objects.all()

            ser = OftenAskedQuestionSerializer(instance=queryset, many=True)

            ret['data'] = ser.data
        except Exception as e:

            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)

    # def retrieve(self, request, *args, **kwargs):
    #
    #     """
    #     课程详细接口
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #
    #     ret = {'code': 1000, 'data': None}
    #
    #     try:
    #         # 课程id=2
    #
    #         pk = kwargs.get('pk')
    #
    #         # 课程详细对象
    #         obj = CourseDetail.objects.filter(course_id=pk).first()
    #         # print(obj)
    #
    #         ser = CourseDetailSerializer(instance=obj, many=False)
    #
    #         ret['data'] = ser.data
    #         print(ser.data)
    #     except Exception as e:
    #         ret['code'] = 1001
    #         ret['error'] = '获取课程失败'
    #     # print(ret)
    #     return Response(ret)



class CourseChapterView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):

        ret = {'code': 1000, 'data': None}
        try:

            queryset = CourseChapter.objects.all()

            ser = CourseChapterSerializer(instance=queryset, many=True)

            ret['data'] = ser.data
        except Exception as e:

            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)



class ArticleView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):

        ret = {'code': 1000, 'data': None}
        try:

            queryset = Article.objects.all()

            ser = ArticleSerializer(instance=queryset, many=True)

            ret['data'] = ser.data
        except Exception as e:

            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}


        try:
            # 课程id=2

            pk = kwargs.get('pk')

            # 课程详细对象
            obj = Article.objects.filter(id=pk).first()
            # print(obj)

            ser = ArticleSerializer(instance=obj, many=False)

            ret['data'] = ser.data
            print(ser.data)
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
            # print(ret)
        return Response(ret)


class CommentView(ViewSetMixin,APIView):

    def list(self, request, *args, **kwargs):

        ret = {'code': 1000, 'data': None}
        try:

            queryset = Comment.objects.all()

            ser = CommentSerializer(instance=queryset, many=True)

            ret['data'] = ser.data
        except Exception as e:

            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)















