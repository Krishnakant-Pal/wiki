from django.shortcuts import render,redirect
from . import util,form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


def index(request):
    """
    Lists all the entries available in the entries by using list_entries from utils.py
    """

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form.NewSearchForm()
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
            "entries": entries,
            "form": form.NewSearchForm()
            
        })
    # display error page if entry does not exist
    else: 
        return render(request, "encyclopedia/error.html",{
            "title": title,
            "form": form.NewSearchForm()
        })


def get_search_query(request):
    """
    Get the search query and return the entry page if exists else search the matching entries and display the results
    """
    if request.method == "POST":
        search_form = form.NewSearchForm(request.POST)

        if search_form.is_valid():
            title = search_form.cleaned_data["title"].lower()
            entries = util.list_entries()
            entries_lower = [entry.lower() for entry in entries]

            # when entry exists return entry page
            if title in entries_lower:
                return entry_page(request, title)
                
            else:
                # shows the matching entries
                matching_entries = []
                for entry in entries:
                    if title in entry.lower():
                        matching_entries.append(entry)

                # return all the matching entries if found
                if len(matching_entries) :
                    return render(request, "encyclopedia/title_search_result.html",{
                        "matching_entries": matching_entries,
                        "form": form.NewSearchForm()
                        })
                # else return the error page
                else:  
                    return entry_page(request, title)
                
    return render(request, "encyclopedia/title_search_result.html",{
        "form": form.NewSearchForm()
        })
    

def new_entry_page(request):
    """Lets users to create a new entry"""
    if request.method == "POST":
        new_entry_page = form.NewEntryForm(request.POST)
        # Validate form if title already exists then display error and return form
        if new_entry_page.is_valid():
            title = new_entry_page.cleaned_data['new_title']
            content = new_entry_page.cleaned_data['content']
            all_present_entries = util.list_entries()

            if title.lower() in all_present_entries:
                return render(request, "encyclopedia/new_entry_page.html",{
                        "new_entry_form": new_entry_page,
                        "form": form.NewSearchForm(),
                        "error": True,
                        "title": title,
                                    })
            # if entry does not exits then save
            else: 
                util.save_entry(title=title,content=content)
                return redirect(reverse("wiki:title", args = [title]))


    return render(request, "encyclopedia/new_entry_page.html",{
        "new_entry_form" : form.NewEntryForm(),
        "form": form.NewSearchForm(),
        "error": False,
    })