from django.http import HttpResponse
from django.shortcuts import redirect, render
import markdown
from . import util
from django import forms


def index(request):
    # search function happenging here bruh!
    if request.method == "POST":
        entries = util.list_entries()
        title = request.POST['q']
        if title.lower() in util.toLowerCaseList(entries):
            return redirect('entry',TITLE=title)
        else:
            filteredEntries=[]
            for entry in util.toLowerCaseList(entries):
                if title in entry:
                    filteredEntries.append(entry)
            return render(request, "encyclopedia/index.html", {
                "entries": filteredEntries
             }) 
    



    # normal home page rendering
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    }) 

def displayEntryContentByTitle(request,TITLE):
    entries = util.list_entries()
    if TITLE.lower() in util.toLowerCaseList(entries):
        md_content = util.get_entry(TITLE)
        html_content = markdown.markdown(md_content)
        return render(request,"encyclopedia/contentLayout.html",{
            "TITLE_ENTRY": TITLE,
            "HTML_ENTRY": html_content
        })
        
    else:
        return render(request,"encyclopedia/contentLayout.html",{
            "TITLE_ENTRY": "ENTRY NOT FOUND",
            "HTML_ENTRY": f"<h1>{TITLE} NOT FOUND</h1>"
        })


    # agar woh entry wrt TITLE HAI TOH  
    # display karo warna create new one 



def addEntry(request):
    if request.method=="POST":
        data = request.POST
        entries = util.list_entries()
        if data['title'].lower() in util.toLowerCaseList(entries):
            print("not saved")
            return render(request,"encyclopedia/contentLayout.html",{
            "TITLE_ENTRY": "ENTRY NOT FOUND",
            "HTML_ENTRY": f"<h1>{data['title']} NOT FOUND</h1>"
            })
        else:
            util.save_entry(data['title'],data['textarea'])
            print("saved")
            return redirect('entry',TITLE= data['title'])
    return render(request,"encyclopedia/add.html")

def editEntry(request, TITLE): #ttile lets say CSS
    #jab edit button click hoga tab ka kam hai ye
    if request.method == "POST":
        updateTextArea = request.POST['textarea']
        util.save_entry(TITLE,updateTextArea)
        return redirect('entry',TITLE=TITLE)


    #normal chal raha hai 
    valueMD = util.get_entry(TITLE)
    return render(request,"encyclopedia/edit.html",{
        "VALUE":valueMD,
        "TITLE":TITLE
    })