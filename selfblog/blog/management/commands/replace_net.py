#coding:utf-8
from django.core.management.base import BaseCommand

from blog.models import Post


class Command(BaseCommand):
    args = 'no'
    help = 'import old post'

    def handle(self, *args, **options):
        replace_all()


def replace_all():
    posts = Post.objects.filter(is_old=True)

    for post in posts:
        #print post.title 
        #处理代码
        index = post.content.find('jasper.net')
        if index > 0:
            print post.title
            post.content = post.content.replace("www.jasper.net", 'www.jasper.com')
            post.content_html = post.content_html.replace("www.jasper.net", 'www.jasper.com')
            post.save()
