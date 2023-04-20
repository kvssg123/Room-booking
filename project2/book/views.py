from django.shortcuts import render
from django.http import HttpResponse
from book.models import Room
from book.forms import SampleForm
# Create your views here.
def index(request):
    form=SampleForm()
    return render(request,'book/index.html',{'form':form})
def detail(request):
    if request.method=='POST':
        # form=SampleForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     roomtype=form.cleaned_data['RoomType']
        #     room=form.cleaned_data['Number']
        #     r=Room.objects.all()
        #     for i in r:
        #         if(i.type==roomtype and i.available_count>int(room)):
        #             c=Room()
        #             c=i
        #             c.delete()
        #             c1=Room(type=roomtype,available_count=i.available_count-int(room),rent_per_day=i.rent_per_day)
        #             c1.save()
        #             context={
        #                 'number':room,
        #                 'roomtype1':roomtype
        #             }
        #             return render(request,'book/detail.html',context)
        #         # count+=1
        roomtype=request.POST.get('Type')
        room=request.POST.get('Rooms')
        room=int(room)
        r=Room.objects.all()
        for i in r:
            if(i.type==roomtype and i.available_count>int(room)):
                c=Room()
                c=i
                c.delete()
                c1=Room(type=roomtype,available_count=i.available_count-int(room),rent_per_day=i.rent_per_day)
                c1.save()
                context={
                    'number':room,
                    'roomtype1':roomtype
                }
        return render(request,'book/detail.html',context)


    return render(request,'book/oops.html')

    
                


        



