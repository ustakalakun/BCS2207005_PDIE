from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from MPP_App.models import MPP, ADMIN, ACTIVITYASSIGN
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404



def activityassign(request):
    if request.method == 'POST':
        activityassignname = request.POST['activityassignname']
        activityassigndate = request.POST['activityassigndate']
        activityassigndate2 = request.POST['activityassigndate2']
        activityassignwork = request.POST['activityassignwork']
        activityassignmpp = request.POST['activityassignmpp']
        activityassignperkara = request.POST['activityassignperkara']

        data = ACTIVITYASSIGN(
            activityassignname=activityassignname,
            activityassigndate=activityassigndate,
            activityassigndate2=activityassigndate2,
            activityassignwork=activityassignwork,
            activityassignmpp=activityassignmpp,
            activityassignperkara=activityassignperkara
        )
        data.save()

        context = {
            'message': 'Activity Assign Saved'
        }
        return render(request, 'activityassign.html', context)
    else:
        return render(request, 'activityassign.html')



# Create your views here.
def login(request):
    return render(request, 'login.html')

def homepage1(request):
    return render(request, 'homepage1.html')

def organization(request):
    return render(request, 'organization.html')

def activity(request):
    return render (request,'activity.html')

def report(request):
    return render(request, 'report.html')


def loginmpp(request):
    if request.method == 'GET':
            return render(request, 'loginmpp.html', {'message':' '})
    else:
        mppId = request.POST['mppId']
        mpppassword = request.POST['mpppassword']
        user = MPP.objects.all().filter(mppId=mppId, mpppassword=mpppassword)
        for x in user:
            if x.mppId==mppId and x.mpppassword==mpppassword:
                url = reverse('homepage2', kwargs={'mppId':mppId})
                return HttpResponseRedirect(url)
        return render(request, 'loginmpp.html', {'message':'Email or password is incorrect.'})
        
def homepage2(request,mppId):
    myMPP=MPP.objects.get(mppId=mppId)
    dict = {
        'myMPP':myMPP,
    }
    return render(request,'homepage2.html',dict)



def loginadmin(request):
    if request.method == 'GET':
            return render(request, 'loginadmin.html', {'message':' '})
    else:
        adminID = request.POST['adminID']
        adminPassword = request.POST['adminPassword']
        user = ADMIN.objects.all().filter(adminID=adminID, adminPassword=adminPassword)
        for x in user:
            if x.adminID==adminID and x.adminPassword==adminPassword:
                url = reverse('homepage3', kwargs={'adminID':adminID})
                return HttpResponseRedirect(url)
        return render(request, 'loginadmin.html', {'message':'Email or password is incorrect.'})



def homepage3(request,adminID):
    myADMIN=ADMIN.objects.get(adminID=adminID)
    dict = {
        'myADMIN':myADMIN,
    }
    return render(request, 'homepage3.html',dict)

def insertactivity(request,mppId):
    myMPP=MPP.objects.get(mppId=mppId)
    dict = {
        'myMPP':myMPP,
    }
    return render(request,'insertactivity.html',dict)

def activitytask(request, mppId):
    activitytask=ACTIVITYASSIGN.objects.all()
    myMPP=MPP.objects.get(mppId=mppId)
    dict={
        'activitytask': activitytask,
        'myMPP':myMPP,
    }
    return render (request,'activitytask.html',dict)

def profilempp(request,mppId):
    myMPP=MPP.objects.get(mppId=mppId)
    profilempp =MPP.objects.filter(mppId=mppId)

    dict = {
        'myMPP':myMPP,
        'viewactivityassign': viewactivityassign,
        'profilempp': profilempp,
    }
    return render(request,'profilempp.html',dict)


def updateprofilempp(request, mppId):
    mpp = get_object_or_404(MPP, mppId=mppId)
    if request.method == 'POST':
        mpp.mppId = request.POST.get('mppId')
        mpp.mpppassword = request.POST.get('mpppassword')
        mpp.mppname = request.POST.get('mppname')
        mpp.save()
        return redirect('profilempp', mppId=mpp.mppId)
    return render(request, 'updateprofilempp.html', {'mpp': mpp})

def profileadmin(request, adminID):
    myADMIN = ADMIN.objects.get(adminID=adminID)
    profileadmin = ADMIN.objects.filter(adminID=adminID)

    context = {
        'myADMIN': myADMIN,
        'profileadmin': profileadmin,
    }
    return render(request, 'profileadmin.html', context)

    
    
def updateprofileadmin(request, adminID):
    admin = get_object_or_404(ADMIN, adminID=adminID)
    if request.method == 'POST':
        admin.adminID = request.POST.get('adminID')
        admin.adminPassword = request.POST.get('adminPassword')
        admin.adminName = request.POST.get('adminName')
        admin.adminEmail = request.POST.get('adminEmail')
        admin.save()
        return redirect('profileadmin', adminID=admin.adminID)
    return render(request, 'updateprofileadmin.html', {'admin': admin})

def viewactivityassign(request, adminID):
    viewactivityassign=ACTIVITYASSIGN.objects.all()
    myADMIN = ADMIN.objects.get(adminID=adminID)
    dict={
        'viewactivityassign': viewactivityassign,
        'myADMIN': myADMIN,
    }
    return render (request,'viewactivityassign.html',dict)

def update_viewactivityassign(request, activityassignname):
    activityassign = get_object_or_404(ACTIVITYASSIGN, activityassignname=activityassignname)

    if request.method == 'POST':
        # Get the updated values from the request
        activityassign.activityassignname = request.POST.get('activityassignname')
        activityassign.activityassigndate = request.POST.get('activityassigndate')
        activityassign.activityassigndate2 = request.POST.get('activityassigndate2')
        activityassign.activityassignperkara = request.POST.get('activityassignperkara')
        activityassign.activityassignwork = request.POST.get('activityassignwork')
        activityassign.activityassignmpp = request.POST.get('activityassignmpp')
        
        activityassign.save()
        return redirect('viewactivityassign')  # Redirect to the activity assignments view

    return render(request, 'update_viewactivityassign.html', {'data': activityassign})


def delete_viewactivityassign(request, activityassignname):
    activityassign = get_object_or_404(ACTIVITYASSIGN, activityassignname=activityassignname)
    activityassign.delete()
    return HttpResponseRedirect(reverse('viewactivityassign'))