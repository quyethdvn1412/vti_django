from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


# class Person(models.Model):
#     name = models.CharField(max_length=128)
#     age = models.IntegerField(int)
#     def __str__(self):
#         return self.name

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)


# class Manufacturer(models.Models):
#     class CarBlue:
#         pass
#     class CarRed:
#         pass

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#     class Meta:
#         abstract = True
 
# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)

# class CommonInfo(models.Model):
#     # ...
#     class Meta:
#         abstract = True
#         ordering = ['name']
# class Student2(CommonInfo):
#     # ...
#     class Meta2(CommonInfo.Meta):
#         db_table = 'student_info'

# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)
#     def __str__(self) -> str:
#         return self.name
 
# class Restaurant(Place):
#     # name = models.CharField(max_length=50)
#     # address = models.CharField(max_length=80)
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.serves_hot_dogs

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return (self.first_name + self.last_name)
class MyPerson(Person):
	# age = models.IntegerField(int)
    class Meta:
        ordering = ["last_name"]
        proxy = True
    def do_something(self):
        # ...
        print('proxy success')

