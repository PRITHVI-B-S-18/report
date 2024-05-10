from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.generic import ListView
from .models import mentor_tb,std_details

def signin(request):
    if(request.method == "POST"):
        uname = request.POST.get('username') # 'username' - from name in html
        pass1 = request.POST.get('pass') # 'pass' - from name in html
        print(uname,pass1)
        user = authenticate(request,username=uname,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Invalid username or password</h1>')
    else:
        return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

lists = mentor_tb.objects.all()
std_detail = std_details.objects.all()

class NameList(ListView):
    model = mentor_tb
    template_name = 'home.html'
    context_object_name = 'lists'
    



class StudentsList(ListView):
    model = std_details
    template_name = "mentorpage1.html"
    context_object_name = "std_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    
    # def post(self,request,*args,**kwargs):
    #     if(request.method == "POST"):
    #         m_id = self.kwargs['pk']
    #         m_points = request.POST.get("pointsDiscussed")
    #         m_approval = request.POST.get("approval")
    #         m_suggest = request.POST.get("SuggestedBy")
    #         m_response = request.POST.get("Responsibility")

    #         update = details(meetId = m_id,points = m_points,approval = m_approval,suggest = m_suggest,response = m_response)
    #         update.save()
    #         return redirect("meetingDetails",pk = m_id)
    #     else:
    #         return render(request,"testapp/meetingDetails.html")

