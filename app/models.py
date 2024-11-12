from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.TextField(max_length=32)
    email = models.TextField(max_length=32)
    phone = models.TextField(max_length=32)
    is_favorite = models.BooleanField()

def create_friend(name, email, phone, is_favorite):
    friend = Friend(name = name, email = email, phone = phone, is_favorite = is_favorite)
    friend.save()
    return friend


def all_friends():
    return Friend.objects.all()


def find_friend_by_name(name):
    for item in Friend.objects.all():
        if item.name == name:
            return item
        else:
            continue

def favorite_friends():
    return Friend.objects.filter(is_favorite = True)

def update_friend_email(name, new_email):
    Friend.objects.filter(name=name).update(email=new_email)
    

def delete_friend(name):
    try:
        obj = Friend.objects.get(name = name) 
        obj.delete()
    except:
        print("error")