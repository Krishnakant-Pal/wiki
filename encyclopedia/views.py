from django.shortcuts import render
from . import util

from django.http import HttpResponse

def index(request):
    """
    Lists all the entries available in the entries by using list_entries from utils.py
    """

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request,title):
    """
    Renders a page for the entry present in the entries and if does not exist then renders error page
    """
    # Get the entry 
    entries = util.get_entry(title)
    
    # display entry page if entry exists
    if entries:
        return render(request, "encyclopedia/entry_page.html",{
            "title": title.capitalize(),
            "entries": entries
            
        })
    # display error page if entry does not exist
    else: 
        return render(request, "encyclopedia/error.html",{
            "title": title
        })
