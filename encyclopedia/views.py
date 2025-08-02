from django.http import HttpResponse
from django.shortcuts import redirect, render
import markdown
from . import util


def index(request):
    # search function happemging here bruh!
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



