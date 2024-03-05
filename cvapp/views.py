from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CvCreate
import os

# Create your views here.
def cvcreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        exam_name1 = request.POST.get('exam_name1')
        exam_board1 = request.POST.get('exam_board1')
        exam_passingyear1 = request.POST.get('exam_passingyear1')
        exam_result1 = request.POST.get('exam_result1')

        exam_name2 = request.POST.get('exam_name2')
        exam_board2 = request.POST.get('exam_board2')
        exam_passingyear2 = request.POST.get('exam_passingyear2')
        exam_result2 = request.POST.get('exam_result2')

        exam_name3 = request.POST.get('exam_name3')
        exam_board3 = request.POST.get('exam_board3')
        exam_passingyear3 = request.POST.get('exam_passingyear3')
        exam_result3 = request.POST.get('exam_result3')

        exam_name4 = request.POST.get('exam_name4')
        exam_board4 = request.POST.get('exam_board4')
        exam_passingyear4 = request.POST.get('exam_passingyear4')
        exam_result4 = request.POST.get('exam_result4')

        experience = request.POST.get('experience')
        extra_curriculam = request.POST.get('extra_curriculam')
        training_name = request.POST.get('training_name')
        training_company = request.POST.get('training_company')
        training_duration = request.POST.get('training_duration')
        training_achevment = request.POST.get('training_achevment')
        training_place = request.POST.get('training_place')
        career_object = request.POST.get('career_object')
        declaration = request.POST.get('declaration')

        image = request.FILES.get('image')
        if image:
            cvcreate = CvCreate.objects.create(name=name, father_name=father_name, mother_name=mother_name, email=email, phone=phone, dob=dob, gender=gender, present_address=present_address, permanent_address=permanent_address, exam_name1=exam_name1, exam_board1=exam_board1, exam_passingyear1=exam_passingyear1, exam_result1=exam_result1, exam_name2=exam_name2, exam_board2=exam_board2, exam_passingyear2=exam_passingyear2, exam_result2=exam_result2, exam_name3=exam_name3,exam_board3=exam_board3, exam_passingyear3=exam_passingyear3, exam_result3=exam_result3,
            exam_name4=exam_name4, exam_board4=exam_board4, exam_passingyear4=exam_passingyear4, exam_result4=exam_result4, experience=experience,extra_curriculam=extra_curriculam, training_name=training_name, training_company=training_company, training_duration=training_duration, training_achevment=training_achevment, training_place=training_place, career_object=career_object, declaration=declaration, image=image)
            cvcreate.save() 

        else:
            cvcreate = CvCreate.objects.create(name=name, father_name=father_name, mother_name=mother_name, email=email, phone=phone, dob=dob, gender=gender, present_address=present_address, permanent_address=permanent_address, 
            exam_name1=exam_name1, exam_board1=exam_board1, exam_passingyear1=exam_passingyear1, exam_result1=exam_result1, exam_name2=exam_name2, exam_board2=exam_board2, exam_passingyear2=exam_passingyear2, exam_result2=exam_result2, exam_name3=exam_name3, exam_board3=exam_board3, exam_passingyear3=exam_passingyear3, exam_result3=exam_result3,exam_name4=exam_name4, exam_board4=exam_board4, exam_passingyear4=exam_passingyear4, exam_result4=exam_result4, experience=experience,extra_curriculam=extra_curriculam, training_name=training_name, training_company=training_company, training_duration=training_duration, training_achevment=training_achevment, career_object=career_object, declaration=declaration)
            cvcreate.save()
            messages.success(request, "CV Seccessfully Created.")
        return redirect('home') 

    return render(request, 'cv_temp/cvcreateform.html')



def cvview(request):
    cvviews = CvCreate.objects.all()
    context = {
        'cvviews' : cvviews
    }
    return render(request, 'cv_temp/cvview.html', context)


def delcvprofile(request, id):
    cvprofile = CvCreate.objects.get(id = id)
    if cvprofile.image:
        if cvprofile.image != 'def.jpg':
            os.remove(cvprofile.image.path)
        cvprofile.delete()
        return redirect('cvview')
    else:
        cvprofile.delete()
        return redirect('cvview')
    


def cvupdate(request, id):
    updatecv = CvCreate.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        exam_name1 = request.POST.get('exam_name1')
        exam_board1 = request.POST.get('exam_board1')
        exam_passingyear1 = request.POST.get('exam_passingyear1')
        exam_result1 = request.POST.get('exam_result1')

        exam_name2 = request.POST.get('exam_name2')
        exam_board2 = request.POST.get('exam_board2')
        exam_passingyear2 = request.POST.get('exam_passingyear2')
        exam_result2 = request.POST.get('exam_result2')

        exam_name3 = request.POST.get('exam_name3')
        exam_board3 = request.POST.get('exam_board3')
        exam_passingyear3 = request.POST.get('exam_passingyear3')
        exam_result3 = request.POST.get('exam_result3')

        exam_name4 = request.POST.get('exam_name4')
        exam_board4 = request.POST.get('exam_board4')
        exam_passingyear4 = request.POST.get('exam_passingyear4')
        exam_result4 = request.POST.get('exam_result4')

        experience = request.POST.get('experience')
        extra_curriculam = request.POST.get('extra_curriculam')
        training_name = request.POST.get('training_name')
        training_company = request.POST.get('training_company')
        training_duration = request.POST.get('training_duration')
        training_achevment = request.POST.get('training_achevment')
        training_place = request.POST.get('training_place')
        career_object = request.POST.get('career_object')
        declaration = request.POST.get('declaration')

        image = request.FILES.get('image')

        if image:
            updatecv.name=name
            updatecv.father_name=father_name
            updatecv.mother_name=mother_name
            updatecv.email=email
            updatecv.phone=phone
            updatecv.dob=dob
            updatecv.gender=gender
            updatecv.present_address=present_address
            updatecv.permanent_address=permanent_address
            updatecv.exam_name1=exam_name1
            updatecv.exam_board1=exam_board1
            updatecv.exam_passingyear1=exam_passingyear1
            updatecv.exam_result1=exam_result1
            updatecv.exam_name2=exam_name2
            updatecv.exam_board2=exam_board2
            updatecv.exam_passingyear2=exam_passingyear2
            updatecv.exam_result2=exam_result2
            updatecv.exam_name3=exam_name3
            updatecv.exam_board3=exam_board3
            updatecv.exam_passingyear3=exam_passingyear3
            updatecv.exam_result3=exam_result3
            updatecv.exam_name4=exam_name4
            updatecv.exam_board4=exam_board4
            updatecv.exam_passingyear4=exam_passingyear4
            updatecv.exam_result4=exam_result4
            updatecv.experience=experience
            updatecv.extra_curriculam=extra_curriculam
            updatecv.training_name=training_name
            updatecv.training_company=training_company
            updatecv.training_duration=training_duration
            updatecv.training_achevment=training_achevment
            updatecv.training_place=training_place
            updatecv.career_object=career_object
            updatecv.declaration=declaration
            
            if updatecv.image != 'def.jpg':
                os.remove(cvupdate.image.path)
            updatecv.image=image
            updatecv.save() 
            return redirect('cvview')
        else:
            updatecv.name=name
            updatecv.father_name=father_name
            updatecv.mother_name=mother_name
            updatecv.email=email
            updatecv.phone=phone
            updatecv.dob=dob
            updatecv.gender=gender
            updatecv.present_address=present_address
            updatecv.permanent_address=permanent_address
            updatecv.exam_name1=exam_name1
            updatecv.exam_board1=exam_board1
            updatecv.exam_passingyear1=exam_passingyear1
            updatecv.exam_result1=exam_result1
            updatecv.exam_name2=exam_name2
            updatecv.exam_board2=exam_board2
            updatecv.exam_passingyear2=exam_passingyear2
            updatecv.exam_result2=exam_result2
            updatecv.exam_name3=exam_name3
            updatecv.exam_board3=exam_board3
            updatecv.exam_passingyear3=exam_passingyear3
            updatecv.exam_result3=exam_result3
            updatecv.exam_name4=exam_name4
            updatecv.exam_board4=exam_board4
            updatecv.exam_passingyear4=exam_passingyear4
            updatecv.exam_result4=exam_result4
            updatecv.experience=experience
            updatecv.extra_curriculam=extra_curriculam
            updatecv.training_name=training_name
            updatecv.training_company=training_company
            updatecv.training_duration=training_duration
            updatecv.training_achevment=training_achevment
            updatecv.training_place=training_place
            updatecv.career_object=career_object
            updatecv.declaration=declaration
            updatecv.save() 
            return redirect('cvview') 
    context = {
        'updatecv': updatecv
    }  

    return render(request, 'cv_temp/updatecv.html', context)