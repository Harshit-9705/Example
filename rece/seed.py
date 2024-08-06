from faker import Faker
from .models import *
import random
fake = Faker()





def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            do = Department.objects.all()
            ri = random.randint(0,len(do)-1)

            department = do[ri]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentId.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
                )

            student_obj.save()

    except Exception as e:
       print(e)



def createMarks(n):
    try:
        student_objs = Student.objects.all()
        for i in student_objs:
            subjects = Subject.objects.all()
            for j in subjects:
                SubjectMarks.objects.create(
                    subject = j,
                    student = i,
                    marks = random.randint(0,100)
                )

    except Exception as e:
        print(e)


from django.db.models import Sum

def addrank():
    
    ranks = Student.objects.annotate(marks = Sum("subjectmarks__marks")).order_by("-marks","student_age")
    current = -1
    i = 1
    for rank in ranks:
        StudentRank.objects.create(
            student = rank,
            student_rank = i
        )
        i = i+1