from django.shortcuts import render
from .forms import registerform, loginform, deleteform, updateform, createform
from .models import registerdata, createdata
from django.http.response import HttpResponse


def register_view(request):
    if request.method == "POST":
        rform = registerform(request.POST)
        if rform.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            mobile = request.POST.get('mobile')
            username = request.POST.get('username')
            password = request.POST.get('password')
            #verifypassword = request.POST.get('verifypassword')
            email = request.POST.get('email')

            data = registerdata(
                fname=fname,
                lname=lname,
                mobile=mobile,
                email=email,
                username=username,
                password=password
            )
            data.save()

            rform = registerform()
            lform = loginform()
            return render(request, 'login.html', {'lform': lform})
    else:
        rform = registerform()
        return render(request, 'register.html', {'rform': rform})


def login_view(request):
    if request.method == 'POST':
        lform = loginform(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            username1 = registerdata.objects.filter(username=username)
            password1 = registerdata.objects.filter(password=password)
            if username1 and password1:
                return render(request, 'homeform.html', {'homeview': homeview})
            else:
                return HttpResponse('Invalid details')
    else:
        lform = loginform
        return render(request, 'login.html', {'lform': lform})


def homeview(request):
    return render(request, 'homeform.html', {'homeview': homeview})


def create_view(request):
    if request.method == 'POST':
        cform = createform(request.POST)
        if cform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_cost = request.POST.get('product_cost')
            product_color = request.POST.get('product_color')
            cust_mobile = request.POST.get('cust_mobile')
            cust_name = request.POST.get('cust_name')
            data = createdata(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_color=product_color,
                cust_mobile=cust_mobile,
                cust_name=cust_name
            )
            data.save()
            cform = createform()
            return render(request, 'create.html', {'cform': cform})

    else:
        cform = createform()
        return render(request, 'create.html', {'cform': cform})


def update_view(request):
    if request.method == 'POST':
        uform = updateform(request.POST)

        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')
            update_data = createdata.objects.filter(product_id=product_id)

            if not update_data:
                return HttpResponse('product data is not available')

            else:
                update_data.update(product_cost=product_cost)
                uform = updateform()
                create_data = createdata.objects.all()
                return render(request, 'product_retrieve.html', {'cdata': create_data})
                #return render(request, 'product_update.html', {'uform': uform})


        else:
            return HttpResponse('Invalid form')
    else:
        uform = updateform()
        return render(request, 'product_update.html', {'uform': uform})


def product_retrieve_view(request):
    create_data = createdata.objects.all()
    return render(request, 'product_retrieve.html', {'cdata': create_data})


def delete_view(request):
    if request.method == 'POST':
        dform = deleteform(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            cdata = createdata.objects.filter(product_id=product_id)
            if not cdata:
                return HttpResponse('product is not available')
            else:
                cdata.delete()
                dform = deleteform()
                return render(request, 'product_delete.html', {'dform': dform})

        else:
            return HttpResponse('Invalid form')
    else:
        dform = deleteform()
        return render(request, 'product_delete.html', {'dform': dform})



"""def search_view(request):
    if request.method == 'POST':
        product_name = request.POST.get ('product_name')
        cdata = createdata.objects.all()
        len_cdata = len(cdata)
        sdata= createdata.objects.filter(product_name__exact=product_name)
        len_sdata = len(sdata)
        return render(request,'create.html',{'cdata':cdata, 'len_cdata': len_cdata,'len_sdata':len_sdata})
    else:
        cdata=  createdata.objects.all()
        len_cdata = len(cdata)
        sdata = createdata.objects.all()
        len_sdata = len(sdata)
        return render(request, 'create.html', {'cdata': cdata, 'len_cdata': len_cdata, 'len_sdata': len_sdata})
        
"""