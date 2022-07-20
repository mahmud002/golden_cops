from django.contrib import admin
from django.urls import path
from home import views 
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path("",views.index, name='home'),
    path("profile",views.profile, name='profile'),
    path("profile2",views.profile2, name='profile2'),
    
    path("my_seller_recit_detail",views.my_seller_recit_detail, name='my_seller_recit_detail'),
    path("market_place",views.market_place, name='market_place'),
    path("buy",views.buy, name='buy'),
    path("market_place_form",views.market_place_form, name='market_place_form'),
    path("delete_product",views.delete_product, name='delete_product'),
    path("crop_details",views.crop_details, name='crop_details'),
    path("my_recits",views.my_recits, name='my_recits'),
    path("my_seller_recit",views.my_seller_recit, name='my_seller_recit'),
    path("full_recit",views.full_recit, name='full_recit'),
    path("pro_rec",views.pro_rec, name='pro_rec'),
    path("mon_rec",views.mon_rec, name='mon_rec'),
    path("blog",views.blog, name='blog'),
    path("blog_details",views.blog_details, name='blog_details'),
    path("blog_form",views.blog_form, name='blog_form'),
    path("delete_blog",views.delete_blog, name='delete_blog'),
    path("delete_comment",views.delete_comment, name='delete_comment'),
    path("<int:id>/",views.edit_blog, name='edit_blog'),
    path("<int:id>/edi",views.edit_pro, name='edit_pro'),
    path("<int:id>",views.edit_crop, name='edit_crop'),
    
    
    path("add",views.add, name='add'),
    path("about_us",views.about_us, name='about_us'),
    path("crop_guide",views.crop_guide, name='crop_guide'),
    path("crop_guide_form",views.crop_guide_form, name='crop_guide_form'),
    path("crop_guide_add",views.crop_guide_add, name='crop_guide_add'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("singup",views.singup, name='singup'),
    path("comment",views.comment, name='comment'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 