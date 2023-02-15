from django.urls import path
from .import views
urlpatterns = [
    path('category', views.categoryView),
    path('product/', views.productViews),
    path('<str:id>/', views.ProductDtailsViews),
    path('addProduct', views.createdProductViews),
    path('addCategory', views.createdCategoryViews),
    path('category/<str:id>/', views.categorytDtailsViews),
    path('createList', views.CreateList),
    path('cartRUD/<str:id>', views.CartUpdatDetailREmove)
 
 
]

