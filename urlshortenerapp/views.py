from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Long
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.
def hello_world(request):
    return HttpResponse("HELLO how are you!!*_'")

def task_t(request):
    context={"year":"2022","attendees":["rahul","abhi","amu"]}
    return render(request,"task.html",context)    

def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }
    if request.method == "POST":
        data = request.POST
        longurl = data['longurl']
        customname = data['custom_name']
        
        try:
            # Only save the customname (slug) in the database
            obj = Long(longurl=longurl, custom_name=customname)
            obj.save()

            # Pass only the slug to the template
            context["longurl"] = longurl
            context["custom_name"] = customname
            context["submitted"] = True
            context["date"] = obj.created_date
            context["clicks"] = obj.visit_count
        except Exception as e:
            print(e)
            context["error"] = True
    else:
        print("USER didn't enter data")
 
    return render(request, "index.html", context)
  

def redirect_url(request, customname):
    try:
        # Use get_object_or_404 for more concise error handling
        obj = get_object_or_404(Long, custom_name=customname)

        # Update the visit count
        obj.visit_count += 1
        obj.save()

        # Redirect to the long URL
        return redirect(obj.longurl)

    except Long.DoesNotExist:
        # Return a 404 error if the customname doesn't exist
        raise Http404("Error 404: This endpoint doesn't exist")
    """
def redirect_url(request,customname):
    row=Long.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint dosen't exist Error!!")
    obj=row[0]
    lonurl=obj.longurl
    obj.visit_count+=1
    obj.save()
    return redirect(lonurl)    
    """
    
def analytics(request):
    rows=Long.objects.all()
    context={
        "rows":rows
    }
    return render(request,"analytics.html",context)