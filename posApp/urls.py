from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('home', views.home, name="home-page"),
    path('tes1', views.tes1, name="tes4"),
    path('login', auth_views.LoginView.as_view(template_name = 'authenticate/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('register', views.register_view, name="register"),
    path('logout', views.logoutuser, name="logout"),
    path('category', views.category, name="category-page"),
    path('manage_category', views.manage_category, name="manage_category-page"),
    path('save_category', views.save_category, name="save-category-page"),
    path('delete_category', views.delete_category, name="delete-category"),
    path('products', views.products, name="product-page"),
    path('manage_products', views.manage_products, name="manage_products-page"),
    path('test', views.test, name="test-page"),
    path('save_product', views.save_product, name="save-product-page"),
    path('delete_product', views.delete_product, name="delete-product"),
    path('transaksi', views.pos, name="pos-page"),
    path('checkout-modal', views.checkout_modal, name="checkout-modal"),
    path('save-pos', views.save_pos, name="save-pos"),
    path('struk', views.salesList, name="sales-page"),
    path('receipt', views.receipt, name="receipt-modal"),
    path('delete_sale', views.delete_sale, name="delete-sale"),
    path('buku', views.produk, name="produk"),
    path('tambahkan_produk', views.tambahkan_produk, name="tambahkan"),
    path('update_produk/<int:id>', views.update_informasi_produk, name="update_produk"),
    ## path('delete_produk/<int:id>', views.delete_produk, name="delete_produks"),
    path('', views.main, name="main"),
    path('stok', views.stok, name="stok"),
    path('search_buku', views.search_buku, name="search_buku"),
    path('main2', views.main2, name="main2"),
    path('about', views.about, name="about"),
    path('informasi_buku/<int:id>', views.informasi_buku, name="informasi_buku"),

    # path('employees', views.employees, name="employee-page"),
    # path('manage_employees', views.manage_employees, name="manage_employees-page"),
    # path('save_employee', views.save_employee, name="save-employee-page"),
    # path('delete_employee', views.delete_employee, name="delete-employee"),
    # path('view_employee', views.view_employee, name="view-employee-page"),
]