from rest_framework import serializers


from app01.models import *

class CourseSerializer(serializers.ModelSerializer):
    """

    给课程表做序列化
    """

    # sub_category=serializers.SerializerMethodField()



    sub_category=serializers.CharField(source='sub_category.name')
    degree_course=serializers.CharField(source='degree_course.name')
    course_img1=serializers.CharField(source='degree_course.course_img')
    brief1=serializers.CharField(source='degree_course.brief')
    total_scholarship=serializers.CharField(source='degree_course.total_scholarship')
    mentor_compensation_bonus=serializers.CharField(source='degree_course.mentor_compensation_bonus')

    # asked_question=serializers.CharField(source='asked_question.question')





    course_type=serializers.CharField(source='get_course_type_display')

    level=serializers.CharField(source='get_level_display')
    status=serializers.CharField(source='get_status_display')
    category=serializers.CharField(source='sub_category.category.name')





    class Meta:
        model = Course
        fields=['name','course_img','sub_category','degree_course','course_type',"brief",


                'level',
                'pub_date',
                'period',
                'order',
                'attachment_path',
                'status',
                'template_id',
                'category',
                'course_img1',
                'brief1',
                'total_scholarship',
                'mentor_compensation_bonus',
                # 'asked_question'

                ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详情
    """

    course=serializers.CharField(source='course.name')

    recommend_courses=serializers.SerializerMethodField()

    teachers=serializers.SerializerMethodField()


    def get_teachers(self,obj):

        queryset=obj.teachers.all()

        return [{'name':i.name,'role':i.get_role_display(),'title':i.title,'signature':i.signature,'image':i.image,'brief':i.brief} for i in queryset]


    def get_recommend_courses(self,obj):

        queryset=obj.recommend_courses.all()

        return [{'name':i.name}  for i in queryset]


    class Meta:
        model=CourseDetail

        fields=[

            'course','hours','course_slogan','video_brief_link','why_study',
            'what_to_study_brief','career_improvement','prerequisite','recommend_courses',
            'teachers',


        ]


class OftenAskedQuestionSerializer(serializers.ModelSerializer):

    """
    常见问题表
    """
    content_type=serializers.CharField(source='content_type.name')
    content_object=serializers.CharField(source='content_object.title')

    class Meta:

        model=OftenAskedQuestion

        fields=['content_type','content_object','question','answer']




class CourseChapterSerializer(serializers.ModelSerializer):
    """

    课程章节
    """
    course=serializers.CharField(source='course.name')
    courseSection=serializers.SerializerMethodField()

    Homework=serializers.SerializerMethodField()


    def get_Homework(self,obj):

        queryset=obj.homework_set.all()

        return [{'title':i.title,'order':i.order,'homework_type':i.get_homework_type_display(),

                 'requirement':i.requirement,"threshold":i.threshold,'recommend_period':i.recommend_period,

                 'scholarship_value':i.scholarship_value,'note':i.note,'enabled':i.enabled


                 } for i in queryset]


    def get_courseSection(self,obj):

        queryset=obj.coursesections.all()


        return [{'name':i.name,'order':i.order,'section_type':i.get_section_type_display(),"section_link":i.section_link,

                 'video_time':i.video_time,"pub_date":i.pub_date,"free_trail":i.free_trail

                 } for i in queryset]



    class Meta:



        model=CourseChapter


        fields=['course','chapter','name','summary','pub_date','courseSection','Homework']



class ArticleSerializer(serializers.ModelSerializer):


    """
    文章表
    """
    source=serializers.CharField(source='source.name')
    article_type=serializers.CharField(source='get_article_type_display')
    status=serializers.CharField(source='get_status_display')

    position=serializers.CharField(source='get_position_display')




    class Meta:


        model=Article

        fields=[
            'title','source','article_type','brief','head_img','content','pub_date',
            'offline_date','status','order','vid','comment_num','agree_num','view_num',
            'collect_num','date','position'
        ]



class CommentSerializer(serializers.ModelSerializer):

    """
    通用评论表
    """
    content_type=serializers.CharField(source='content_type.name')
    content_object=serializers.CharField(source='content_object.title')
    account=serializers.CharField(source='account.username')

    class Meta:

        model=Comment
        fields=['content_type','object_id','content_object','p_node','content','account',
                'disagree_number','disagree_number','date'

        ]



