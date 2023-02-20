from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        home = Home.objects.all()
        phone = Phone.objects.all()
        hello = Hello.objects.all()
        story = Story.objects.all()
        info = Info.objects.all()
        partner = Partner.objects.all()
        project = Project.objects.all()
        all_info = All_Info.objects.all()
        first_service = First_Service.objects.all()
        second_service = Second_Service.objects.all()
        third_service = Third_Service.objects.all()
        fourth_service = Fourth_Service.objects.all()

        return render(request, self.template_name, {
            'home': home, 'phone':phone, 'hello':hello, 'story':story, 'info':info, 'partner':partner, 'project':project, 'all_info':all_info, 
            'first_service':first_service, 'second_service':second_service, 'third_service':third_service, 'fourth_service':fourth_service
            
            })