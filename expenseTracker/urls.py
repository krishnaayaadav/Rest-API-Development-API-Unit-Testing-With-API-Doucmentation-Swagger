
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
urlpatterns = [
   path('admin/', admin.site.urls),
   path('expense/', include('expenseApp.urls')),

   # api documentation here
   path('expense/api/schema/', SpectacularAPIView().as_view(), name='schema'),
   path('expense/api/docs/',SpectacularRedocView().as_view(url_name="schema") ),
   path('expense/api/documentation/',SpectacularSwaggerView().as_view(url_name="schema") ),

]
