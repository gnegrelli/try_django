import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), True)
