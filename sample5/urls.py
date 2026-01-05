"""
URL configuration for sample5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app3 import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('registeration',views.registeration,name='registeration'),
    path('register',views.register,name='register'),
    path('user_create',views.user_create,name='user_create'),
    path('login',views.login,name='login'),
    path('forgot', views.forgot_password, name="forgot"),
    path('reset/<token>', views.reset_password, name='reset_password'),
    path('user_page',views.user_page,name='user_page'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('logout',views.logout,name='logout'),
    path('view_user',views.view_user,name='view_user'),
    path('search_user',views.search_user,name='search_user'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('artist_create',views.artist_create,name='artist_create'),
    path('artist_page',views.artist_page,name='artist_page'),
    path('view_artist',views.view_artist,name='view_artist'),
    path('delete_artist/<int:id>',views.delete_artist,name='delete_artist'),
    path('userview_artist',views.userview_artist,name='userview_artist'),
    path('view_artprofile',views.view_artprofile,name='view_artprofile'),
    path('search_artworker',views.search_artworker,name='search_artworker'),
    path('craftworker_page',views.craftworker_page,name='craftworker_page'),
    path('craft_create',views.craft_create,name='craft_create'),
    path('delete_craft',views.delete_craft,name='delete_craft'),
    path('view_craft',views.view_craft,name='view_craft'),
    path('userview_craft',views.userview_craft,name='userview_craft'),
    path('search_craftworker',views.search_craftworker,name='search_craftworker'),
    path('artproduct_create',views.artproduct_create,name='artproduct_create'),
    path('view_artproduct',views.view_artproduct,name='view_artproduct'),
    path('userview_artproduct/<str:id>',views.userview_artproduct,name='userview_artproduct'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('craft_profile',views.craft_profile,name='craft_profile'),
    path('craftproduct_create',views.craftproduct_create,name='craftproduct_create'),
    path('view_craftproduct',views.view_craftproduct,name='view_craftproduct'),
    path('userview_craftproduct/<str:id>',views.userview_craftproduct,name='userview_craftproduct'),
    path('adminview_craft_profile/<int:id>',views.adminview_craft_profile,name='adminview_craft_profile'),
    path('adminview_craftproduct/<str:id>',views.adminview_craftproduct,name='adminview_craftproduct'),
    path('adminview_art_profile/<int:id>', views.adminview_art_profile, name='adminview_art_profile'),
    path('adminview_artproduct/<str:id>', views.adminview_artproduct, name='adminview_artproduct'),
    path('user_search_craftworker',views.user_search_craftworker,name='user_search_craftworker'),
    path('user_search_artworker', views.user_search_artworker, name='user_search_artworker'),
    path('adminview_userprofile/<int:id>',views.adminview_userprofile,name='adminview_userprofile'),
    path('addtocart/<int:pid>/<str:ptype>',views.addtocart,name='addtocart'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('addtowishlist/<int:pid>/<str:ptype>', views.addtowishlist, name='addtowishlist'),
    path('view_wishlist', views.view_wishlist, name='view_wishlist'),
    path('move_to_cart/<int:wid>/', views.move_to_cart, name='move_to_cart'),
    path('increment/<int:cid>',views.increment,name='increment'),
    path('decrement/<int:cid>',views.decrement,name='decrement'),
    path('checkout',views.checkout,name='checkout'),
    path('place_order',views.place_order,name='place_order'),
    path('payment_success',views.payment_success,name='payment_success'),
    path('order_details',views.order_details,name='order_details'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('update_order_status/<int:oid>/', views.update_order_status, name='update_order_status'),
    path('samform',views.samform,name='samform'),
    path('update_artdata/<int:id>',views.update_artdata,name='update_artdata'),
    path('update_craftdata/<int:id>',views.update_craftdata,name='update_craftdata'),
    path('update_craftproduct/<int:id>',views.update_craftproduct,name='update_craftproduct'),
    path('update_userprofile/<int:id>',views.update_userprofile,name='update_userprofile'),
    path('update_artproduct/<int:id>',views.update_artproduct,name='update_artproduct'),
    path('artist_viewuser',views.artist_viewuser,name='artist_viewuser'),
    path('craftworker_viewuser',views.craftworker_viewuser,name='craftworker_viewuser'),
    path('send_feedback',views.send_feedback,name='send_feedback'),
    path('feedback_success',views.feedback_success,name='feedback_success'),
    path('view_feedbacks',views.view_feedbacks,name='view_feedbacks'),
    path('reply_feedback/<int:feedback_id>',views.reply_feedback,name='reply_feedback'),
    path('my_feedbacks',views.my_feedbacks,name='my_feedbacks'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)