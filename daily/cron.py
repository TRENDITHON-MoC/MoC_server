from .models import *
from django.utils import timezone
from datetime import timedelta
import datetime
import calendar

def create_monthly_instance():
    today = timezone.now().date()
    _, last_day = calendar.monthrange(today.year, today.month)
    start_date = today.replace(day=1)
    end_date = today.replace(day=last_day)
    Monthly.objects.create(start_on=start_date, finish_on=end_date)


def create_weekly_instance():
    today = timezone.now().date()
    start_date = today - datetime.timedelta(days=today.weekday())
    end_date = start_date + datetime.timedelta(days=6)
    Weekly.objects.create(start_on=start_date, finish_on=end_date)


def create_daily_instance():
    Daily.objects.create(day = timezone.now())


def select_popular_post():
    yesterday = timezone.now().date() - timedelta(days=1)
    day = Daily.objects.prefetch_related('posts').get(day = yesterday)
    posts = day.posts

    popular_posts = posts.order_by('-like_cnt')[:5]
    for pp in popular_posts:
        PopularPost(daily = day, post = pp).save()
    