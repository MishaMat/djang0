from django.db import models


# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()


class NewsModel(models.Model):
    title = models.CharField(max_length=30)
    main_info = models.CharField(max_length=1000)
    create_at = models.DateField(auto_now_add=True)
    edit_at = models.DateField(auto_now=True)
    flag = models.ForeignKey('FlagModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FlagModel(models.Model):
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.status


class CommentModel(models.Model):
    username = models.CharField(max_length=25)
    comment = models.CharField(max_length=100)
    news = models.ForeignKey('NewsModel', default=0, on_delete=models.CASCADE)
