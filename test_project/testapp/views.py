from django.shortcuts import render
from . import models

@csrf_exempt
def sample(request):
    if request.method == "POST":
        mailone = request.POST["mailone"]
        u_name = request.POST["u_name"]

        models.Mail_Table.objects.create(email = mailone, u_name = u_name)

        #get_mail = Mail_Table.objects.get(email=mailone)
        #get_mail.email = mailone
        #get_mail.save()
        #print(get_mail)
        #get_mail_details = Mail_Table.objects.filter(email=mailone)
        #print(get_mail_details)

        return render(request,"sample.html",{"result":mailone})
    return render(request,"sample.html")
