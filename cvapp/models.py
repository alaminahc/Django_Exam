from django.db import models

# Create your models here.
class CvCreate(models.Model):
    GENDER = (
        ('Male' , 'MALE'),
        ('Female' , 'FEMALE'),
        ('Others' , 'OTHERS'),
    )

    name = models.CharField(max_length = 25)
    father_name = models.CharField(max_length = 25)
    mother_name = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 30,  blank = True, null = True)
    phone = models.CharField(max_length = 15)
    dob = models.DateField()
    gender = models.CharField(choices = GENDER, max_length=max(len(choices[0]) for choices in GENDER), default = 'MALE')
    
    present_address = models.CharField(max_length= 100, blank = True, null = True)
    permanent_address = models.CharField(max_length= 100, blank = True, null = True)

    exam_name1 = models.CharField(max_length= 50, blank = True, null = True)
    exam_board1 = models.CharField(max_length=15, blank = True, null = True)
    exam_passingyear1 = models.CharField(max_length=4, blank = True, null = True)
    exam_result1 = models.CharField(max_length=3, blank = True, null = True)

    exam_name2 = models.CharField(max_length= 50, blank = True, null = True)
    exam_board2 = models.CharField(max_length=15, blank = True, null = True)
    exam_passingyear2 = models.CharField(max_length=4, blank = True, null = True)
    exam_result2 = models.CharField(max_length=3, blank = True, null = True)

    exam_name3 = models.CharField(max_length= 50, blank = True, null = True)
    exam_board3 = models.CharField(max_length=15, blank = True, null = True)
    exam_passingyear3 = models.CharField(max_length=4, blank = True, null = True)
    exam_result3 = models.CharField(max_length=3, blank = True, null = True)

    exam_name4 = models.CharField(max_length= 50, blank = True, null = True)
    exam_board4 = models.CharField(max_length=15, blank = True, null = True)
    exam_passingyear4 = models.CharField(max_length=4, blank = True, null = True)
    exam_result4 = models.CharField(max_length=3, null = True, blank = True)

    experience = models.CharField(max_length= 150, blank = True, null = True)
    extra_curriculam = models.CharField(max_length= 150, blank = True, null = True)

    training_name = models.CharField(max_length= 50, blank = True, null = True)
    training_company = models.CharField(max_length= 50, blank = True, null = True)
    training_duration = models.CharField(max_length= 50, blank = True, null = True)
    training_achevment = models.CharField(max_length= 50, blank = True, null = True)
    training_place = models.CharField(max_length= 50, blank = True, null = True)

    career_object = models.CharField(max_length= 150, blank = True, null = True)

    declaration = models.CharField(max_length= 250, blank = True, null = True)
 

    image = models.ImageField(upload_to='image/', default = 'def.jpg', blank = True, null = True)

    def __str__(self):
        return self.name