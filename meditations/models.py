from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Meditation(models.Model):
    med_ID = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100)
    med_Lname = models.CharField(max_length=100)
    med_type = models.CharField(max_length=100)
    med_description = models.CharField(max_length=500)
    meditation_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('med_list', args=[str(self.id)])


class Meditation_Page(models.Model):
    med_page_url = models.CharField(max_length=150)
    med_page_details = models.CharField(max_length=150)
    meditation_image = models.ImageField(upload_to='images/', null=True,
                                     blank=True)
    def __str__(self):
        return self.med_page_url


class MyUser(models.Model):
    user_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)
    # User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Page_Visit(models.Model):
    visit_ID = models.AutoField(primary_key=True)
    visit_date_time = models.DateField(auto_now_add=True)
    med_visitor_IP = models.GenericIPAddressField()
    med_page_url = models.URLField()
    user_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    med_ID = models.CharField(max_length=100)

    def __str__(self):
        return f"Visit ID: {self.visit_ID}, URL: {self.med_page_url}"

class QuoteOfTheDay(models.Model):
    quote = models.TextField()

    def __str__(self):
        return self.quote

class About(models.Model):
    about_page_ID = models.AutoField(primary_key=True)
    creator_ID = models.DateField(auto_now_add=True)
    user_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Profile(models.Model):
    profile_page_ID = models.AutoField(primary_key=True)
    profile_ID = models.CharField(max_length=100)
    user_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class ForgotPassword(models.Model):
    forgot_page_ID = models.AutoField(primary_key=True)
