from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import sqlite3
from . forms import AddJobForm

def addjob(request):
    if request.method == "GET":
        return render(request,'add_job.html')
    else:
        #process date and redirect to list ofjobs
        title = request.POST['title']
        minsal = request.POST['minsal']
        try:
            con = sqlite3.connect(r"C:\classroom\python\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs(title,minsal) values (?,?)",(title,minsal))
            con.commit()
            return HttpResponseRedirect("/demo/jobs/")
        except:
            return HttpResponse("<h1>Sorry! Could not add job due to some error </h1>")


def list_job(request):
    con = sqlite3.connect(r"c:\classroom\python\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs ")
    jobs = cur.fetchall()

    #con.close()
    return render(request, 'list_jobs.html',{'jobs': jobs})


def addjob_with_form(request):
    if request.method == "GET":
        f = AddJobForm()
        return render(request,'add_job_form.html',{'form'  : f})
    else:
        #process date and redirect to list ofjobs
        f = AddJobForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            minsal = f.cleaned_data['minsal']
            try:
                con = sqlite3.connect(r"C:\classroom\python\hr.db")
                cur = con.cursor()
                cur.execute("insert into jobs(title,minsal) values (?,?)",(title,minsal))
                con.commit()
                return HttpResponseRedirect("/demo/jobs/")
            except:
             return HttpResponse("<h1>Sorry! Could not add job due to some error </h1>")
        else:
            return render(request,'add_job_form.html',{'form':f})