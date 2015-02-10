from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from article.models import Document
from article.forms import DocumentForm
# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.template import Context
import random, re, os, datetime, time, urllib
from django.contrib.auth.decorators import login_required
from article.models import Clients
from article.models import ClientsData
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def home(request,template='article/add_article.html'):
    #data={'First_name':Fname,'last_name':Lname,'designation':Designation}
    author = 'author'
    article = 'article'
    image ='images'
    video = 'videos'
    contact ='contacts'
    data={'author':author,'article':article,'images':image,'videos':video,'contacts':contact}
    return render_to_response('home.html',data,context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        name = request.POST['subject']
        user_mail = request.POST['email']
        subject = request.POST['subject']+"  from: "+user_mail
        message = request.POST['message']
        sender = 'chandruit15@gmail.com'
        recipients = ['chandruit15@gmail.com']
        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)
        return render_to_response('success_mail.html',context_instance=RequestContext(request))
    else:
        return render_to_response('home.html',context_instance=RequestContext(request))
    
def calculate(request):
    data={}
    client = Clients.objects.all()
    data['client'] = client
    return render_to_response('calculate.html',data,context_instance=RequestContext(request))


def clients_data(request,pk=0):
    data = {}
    name = Clients.objects.distinct().get(id=pk)
    list = []
    accounts = ClientsData.objects.filter(name_id=pk).select_related('accounts')
    for x in accounts:
        list.append(x.name)
    data['client'] = accounts
    data['list'] = list
    data['name'] = name
    return render_to_response('clients_data.html',data,context_instance=RequestContext(request))  
    
def report(request):
    status = request.POST['select_client']
    if status == '0':
        date=request.POST['date']
        data = {}
        cleint_rep_data = ClientsData.objects.filter(added_date=date)
        data['cleint_rep_data'] = cleint_rep_data
        return render_to_response('clients_report.html',data,context_instance=RequestContext(request))
    else:
        date=request.POST['date']
        data = {}
        cleint_rep_data = ClientsData.objects.filter(added_date=date,name_id=status)
        data['cleint_rep_data'] = cleint_rep_data
        
        return render_to_response('clients_report.html',data,context_instance=RequestContext(request))
    
def report2(request):
    status = request.POST['select_client']
    if status == '0':
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        data = {}
        cleint_rep_data = ClientsData.objects.filter(added_date__range=[start_date, end_date])
        data['cleint_rep_data'] = cleint_rep_data
        return render_to_response('clients_report2.html',data,context_instance=RequestContext(request))
    else:
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        data = {}
        cleint_rep_data = ClientsData.objects.filter(added_date__range=[start_date, end_date],name_id=status)
        data['cleint_rep_data'] = cleint_rep_data
        return render_to_response('clients_report2.html',data,context_instance=RequestContext(request))
    
def date(request):
    data = {}
    clients = Clients.objects.all()
    data['clients'] =clients
    return render_to_response('date_picker.html',data,context_instance=RequestContext(request))
    

def download(request,pk=0):
    doc = Document.objects.distinct().get(id=pk)
    fname=doc.docfile.name
    import urllib;   
    url ="http://192.168.1.59:8005/media/"+fname
    opener = urllib.urlopen(url);  
    mimetype = "application/octet-stream"
    response = HttpResponse(opener.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=aktel.rar"
    return response 
