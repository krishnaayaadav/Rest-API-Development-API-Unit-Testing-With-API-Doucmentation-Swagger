from django.urls import path, include

urlpatterns = [

    # api end points
    path('api/', include('expenseApp.apiFiles.api_urls')),
]