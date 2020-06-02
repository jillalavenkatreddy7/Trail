from django.shortcuts import render
from .models import OnlinePower
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def showIndex(request):
    return render(request,"welcome.html")
def newMeter(request):
    return render(request,"new-meter.html")
def addBill(request):
    return render(request,"add_bill.html")
def billPayment(request):
    return render(request,"payment.html")

def saveMeter(request):
    meter_number=request.POST.get("mn")
    customer_name=request.POST.get("cname")
    meter_type=request.POST.get("tm")
    OnlinePower(meter_number=meter_number,customer_name=customer_name,Meter_type=meter_type).save()
    messages.success(request,"new meter added")
    return redirect('new')
def saveBill(request):
    data=request.POST.get("mn")
    btype=request.POST.get("view")
    if btype=="view":
        viewdata=OnlinePower.objects.filter(meter_number=data)
        return render(request, "add_bill.html", {"viewdata": viewdata})
    if btype=="save":
        cname=request.POST.get("c1")
        mtype=request.POST.get("m1")
        units=request.POST.get("un")
        OnlinePower(meter_number=data,customer_name=cname,Meter_type=mtype,units=units).save()
        return render(request,"add_bill.html",{"message":"details are saved"})


def viewDetails(request):
    viewdata=request.GET.get("view")
    seedata=OnlinePower.objects.filter(meter_number=viewdata)
    return render(request,"add_bill.html",{"seedata":seedata})


def paymentDetails(request):
    meter_num=request.POST.get("mnu")
    data = OnlinePower.objects.filter(meter_number=meter_num)
    industry_type=15.25
    commercial=10.15
    residence=5.10
    type=request.POST.get("type")
    units=(request.POST.get("unit"))
    if type=="Industry":
        total=industry_type*(units)
        print(".........................")
        print(total)
        return render(request, "payment.html", {"data": data, "total": total})
    elif type=="Commercial":
        total=commercial*float(units)
        return render(request, "payment.html", {"data": data, "total": total})
    elif type=="Residence":
        total=residence*float(units)
        return render(request, "payment.html", {"data": data, "total": total})
    else:
        return render(request, "payment.html", {"data": data})

    #return render(request,"payment.html",{"data":data,"total":total})