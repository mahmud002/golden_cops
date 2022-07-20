from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime
from .forms import *

        

def index (request):
    return render(request,'firsthtml.html')
def profile (request):
    if request.user.is_authenticated:
        data=Profile.objects.all()
        data2=Blog.objects.all()
        data3=Crop.objects.all()
        c=Comment.objects.all()
        a=[]
        b=[]
        
        for temp in data2:
            s=str(temp.username)
            if s==request.user.username:
                a.append(temp)     
            
        for temp in data3:
            s=str(temp.username)
            if s==request.user.username:
                b.append(temp)     
            
        return render(request,'profile.html',{'data':data, 'a':a,'b':b,'c':c})
    else:
        return HttpResponse("Please Login First")
    #return HttpResponse("profile")

def profile2 (request):
    if request.user.is_authenticated:

        target=request.POST.get('System')
        data=Profile.objects.all()
        
        for temp in data:
            s1=str(temp.user)
            if s1==target:
                p=temp
                
                
 
        data2=Blog.objects.all()
        data3=Crop.objects.all()
        a=[]
        b=[]
        
        for temp in data2:
            s=str(temp.username)
            s2=str(p.user)
            if s==s2:
                a.append(temp)
                
            
        for temp in data3:
            s=str(temp.username)
            s2=str(p.user)
            if s==s2:
                b.append(temp)
        print(p)
        print(type(p))
        print("______THis")
        return render(request,'profile2.html',{'temp':p,'a':a,'b':b})
        
    else:
        return HttpResponse("Please Login First")



##############      MArket Place #################
def market_place (request):
   
        data=Crop.objects.all()
        return render(request,'market_place.html',{'data':data})

    #return HttpResponse("I am market_place")
def market_place_form (request):
       
        form=MarketPlaceForm()
        if request.method =='POST':
            form=MarketPlaceForm(request.POST,request.FILES)
            
            if form.is_valid():
                instance=form.save(commit=False)
                instance.username=request.user.profile
                form.save()
               
            return redirect('market_place')
        return render(request,'blog_form.html',{'form':form})
def buy (request):
        if request.user.is_authenticated:
            id1=request.POST.get('BuySystem')

            data=Crop.objects.all()

            for temp in data:
                s1=str(temp)
    
                if s1==id1:
                    id2=temp
                     
            name=request.user.profile
            new_post=Purchase(crop=id2, username=name) 
            new_post.save()
            

            return redirect('market_place')
        else:
            return HttpResponse("Please Login First")



def my_recits (request):

    data=Purchase.objects.all()
    a=[]
    for temp in data:
        s=str(temp.username)
        if s==request.user.username:
            a.append(temp)
    
            
    return render(request,'my_recits.html',{'a':a})
     


def full_recit (request):
        
        if request.user.is_authenticated:
            target=request.POST.get('RecitSystem2')
     
            data=Purchase.objects.all()
            for temp in data:
                s=str(temp.id)
                if target==s:
                    total=temp.crop.price*temp.crop.unit
 
                    return render(request,'recit.html',{'temp':temp,'total':total})
           
        else:
            return HttpResponse("Please Login First")
def pro_rec (request):
        
        if request.user.is_authenticated:
            target=request.POST.get('PRSystem')

            data=Purchase.objects.all()
            for temp in data:
                s=str(temp)
                if target==s:
                    id2=temp
            id2.d_status="Recived"
            id2.save()

            return redirect('profile')
           
        else:
            return HttpResponse("Please Login First") 
def mon_rec (request):
        
        if request.user.is_authenticated:
            target=request.POST.get('MRSystem')
            print("target")
            print(type(target))
            print(target)
            data=Purchase.objects.all()
            for temp in data:
                s=str(temp)
                if target==s:
                    id2=temp
            id2.p_status="Recived"
            id2.save()
            print(id2.p_status)

            return redirect('my_seller_recit')
           
        else:
            return HttpResponse("Please Login First") 
def my_seller_recit (request):
        
        if request.user.is_authenticated:
            data=Purchase.objects.all()
            a=[]
            for temp in data:
                s=str(temp.crop.username)
                if s==request.user.username:
                    print(temp.crop.username)
                    a.append(temp)
    
            
            return render(request,'my_seller_recit.html',{'a':a})
           
        else:
            return HttpResponse("Please Login First") 

def comment (request):
        
        if request.user.is_authenticated:
            pk=request.POST.get('System2')
           
            cmt=request.POST.get('comment')
          
            data=Blog.objects.all()
            for temp in data:
                s=str(temp.id)
                if s==pk:
                    id2=temp
            blog=id2
            post=cmt
            user=request.user
            new_post=Comment(blog=blog, post=post, user=user)
            new_post.save()
         
            return redirect('blog')
        else:
            return HttpResponse("Please Login First") 
def my_seller_recit (request):
        
        if request.user.is_authenticated:
            data=Purchase.objects.all()
            a=[]
            for temp in data:
                s=str(temp.crop.username)
                if s==request.user.username:
                    print(temp.crop.username)
                    a.append(temp)
    
            
            return render(request,'my_seller_recit.html',{'a':a})
           
        else:
            return HttpResponse("Please Login First") 
def my_seller_recit_detail (request):
        
        if request.user.is_authenticated:
            target=request.POST.get('Seller1')
            print(target)
            print("Target")
     
            data=Purchase.objects.all()
            for temp in data:
                s=str(temp.id)
                if target==s:
                    total=temp.crop.price*temp.crop.unit
                    print(total)
                    return render(request,'my_seller_recit_detail.html',{'temp':temp,'total':total})
           
        else:
            return HttpResponse("Please Login First")

def delete_product (request):
        if request.user.is_authenticated:
            target=request.POST.get('System')
     
            data=Crop.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('profile')
        else:
            return HttpResponse("Please Login First")
def crop_details (request):
    if request.user.is_authenticated:
        pk=request.POST.get('CropSystem2')
        
        data=Crop.objects.all()
        data2=Profile.objects.all()
        print(pk)
        for temp in data:
            id=str(temp.id)
            if pk == id:
                for temp2 in data2:
                    s1=str(temp.username)
                    s2=str(temp2.user)

                    if s1==s2:
                        print(temp2)
                        print(type(temp2))
                        print("_______________________________")
                        return render(request,'crop_details.html',{'temp':temp,'temp2':temp2})
        
    else:
        return HttpResponse("Please Login First")

############ Blog ###############
def delete_blog (request):
        if request.user.is_authenticated:
            target=request.POST.get('System')
            print(target)
            data=Blog.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('profile')
        else:
            return HttpResponse("Please Login First")
def delete_comment (request):
        if request.user.is_authenticated:
            target=request.POST.get('Comment')
            print(target)
            data=Comment.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('blog')
        else:
            return HttpResponse("Please Login First")


def blog (request):

       
        data=Blog.objects.all()
       
        return render(request,'blog.html', {'data':data})

def blog_details (request):
    if request.user.is_authenticated:
        pk=request.POST.get('System2')
        
        data=Blog.objects.all()
        data2=Profile.objects.all()
        data3=Comment.objects.all()
        a=[]
        for temp in data:
            id=str(temp.id)

            if pk == id:
                for temp3 in data3:
                    c1=str(temp3.blog)
                    c2=str(temp)
                    if c1==c2:
                        a.append(temp3)
 
                for temp2 in data2:
                    s1=str(temp.username)
                    s2=str(temp2.user)
                    print(s1)
                    print(s2)
                    if s1==s2:
                
                
                        return render(request,'blog_details.html',{'temp':temp,'temp2':temp2,'a':a})
                
    else:
        return HttpResponse("Please Login First")

def blog_form (request):
    if request.user.is_authenticated:       
        form=BlogForm()
        if request.method =='POST':
            form=BlogForm(request.POST,request.FILES)
            
            if form.is_valid():
                instance=form.save(commit=False)
                print("User")
                print(instance)
                instance.username=request.user.profile
                form.save()
               
            return redirect('blog')
        return render(request,'blog_form.html',{'form':form})
    else:
        return HttpResponse("Please Login First")
def edit_crop (request,id):
        if request.user.is_authenticated:
            if request.method=='POST':
                pi=Crop.objects.get(pk=id)
                fm=MarketPlaceForm(request.POST,request.FILES, instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

            else:
                pi=Crop.objects.get(pk=id)
                fm=MarketPlaceForm(instance=pi)

            return render(request,'crop_edit.html',{'form':fm})

        else:
            return HttpResponse("Please Login First")

def edit_blog (request,id):
        if request.user.is_authenticated:
            if request.method=='POST':
                pi=Blog.objects.get(pk=id)
                fm=BlogForm(request.POST,request.FILES, instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

            else:
                pi=Blog.objects.get(pk=id)
                fm=BlogForm(instance=pi)

            return render(request,'blog_edit.html',{'form':fm})

        else:
            return HttpResponse("Please Login First")


def edit_pro (request,id):
        if request.user.is_authenticated:
            
            if request.method=='POST':
                pi=Profile.objects.get(pk=id)

                fm=ProfileForm(request.POST, request.FILES,instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

            else:
                pi=Profile.objects.get(pk=id)
                
                fm=ProfileForm(instance=pi)

            return render(request,'profile_edit.html',{'form':fm})

        else:
            return HttpResponse("Please Login First")


 
def add(request):
    #get the name
    name=request.user.profile
   # image=request.FILES('image')
    
    post1=request.GET.get('post')
    date=request.GET.get('date')
    print(name)
    
   
    #create an object
    new_post=Blog(username=name, post=post1)
    #save it
    new_post.save()
    #redirect blog
    return redirect('blog')
def crop_guide_form (request):
    form=CropGuideForm()
    if request.method =='POST':
        form=CropGuideForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crop_guide')
    return render(request,'crop_guide_form.html',{'form':form})
def crop_guide_add(request):
    #get the name
    title=request.GET.get('Title')
    post1=request.GET.get('post')
  
    new_post=CropGuide(title=title, post=post1)
    #save it
    new_post.save()
    #redirect blog
    return redirect('crop_guide')
   

    #return HttpResponse("I am Help")
def about_us (request):

    data=Developer.objects.all()

    return render(request,'about_us.html', {'data':data})
    #return HttpResponse("I am About us")
def crop_guide (request):
 
        data=CropGuide.objects.all()
        return render(request,'crop_guide.html', {'data':data})


def login (request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        print(username1)
        user=authenticate(username=username1,password=password1)
        p=Profile.objects.all()
        if user is None:
            return redirect('login')
            
        else: 
            auth.login(request, user)
            flag=0
            for temp in p:
                s1=str(temp.user)
                s2=str(username1)
                if s1==s2:
                    flag=1
            if flag==0:
                new_pro=Profile(user=request.user)
                new_pro.save()

            return redirect('/')
            
    
    else:    
         return render(request,'login.html')


def logout (request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponse("You logout successfully")
    else:
        return HttpResponse("Please Login First")

def singup (request):
    if request.method == 'POST':
      form=UserCreationForm(request.POST)

      if form.is_valid():
          form.save()
          return redirect('login')
    else:
        form=UserCreationForm()
    return render (request,'singup.html',{'form': form})
