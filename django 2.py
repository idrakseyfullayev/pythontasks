# #                                              Django


# # MVC(Model,View,Controller) - basqa dillerde
# # MVT(Model,View,Template) - Python dilinde

# # pip install pipenv  -  pipenv yukleyir   (virtual muhit)?????????????????????/
# # pip install django  -  django-nu yukleyir
# # django-admin startproject <name> - proyekt yaradir  (django-admin.py)?????????????
# # cd <project_name>  - proyektin qovluguna daxil olur
# # python manage.py startapp <app_name>  -  app yaradir (django-admin startapp <app_name> - app yaradir)

# # python manage.py makemigrations - database cedvellerini hazirlayir
# # python manage.py migrate -   database cedvellerini yaradir
# # python manage.py createsuperuser - super istifadeci yaradir
# # python manage.py changepassword <username> - super istifadecinin parolunu yenileyir
# # python manage.py runserver - serveri aktivlesdirir


# # pip install <kitabxana adi>


# # 1. app yaratdiqdan sonra app-in adini(meselen film) proyektin settings.py-da:
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'film',
# ]


# # 2. app-in adini proyektin urls.py-da:
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('film/', include('film.urls')),
# ]


# # 3. Views.py yazdigimiz def() funksiyalarinin adini app-in urls.py-da:
# from django.urls import path, include
# from film import views

# app_name = 'film'

# urlpatterns = [
#     path('index/', views.IndexView.as_view(), name='index'),
#     path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
#     path('actor_details/<int:id>/', views.actor_details, name='actor_details'),
#     path('actors/<int:id>/', views.actors, name='actors')
# ]


# # 3.1 app-n modelleri models.py qurulur:
# from django.db import models

# class ActorModel(models.Model):
#     poster = models.ImageField(upload_to='posters/')
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     about = models.TextField()
    
#     class Meta:
#         verbose_name = "Actor"

#     def __str__(self) -> str:
#         return self.name + " " + self.surname


# class FilmModel(models.Model):
#     poster = models.ImageField(upload_to='posters/')
#     video = models.FileField(upload_to='films/')
#     views_number = models.IntegerField(default=0)
#     name = models.CharField(max_length=256, help_text="zehmet olmasa simbol daxil edin")
#     rating = models.FloatField(default=0)
#     pub_date = models.DateField()
#     about = models.TextField()
#     actors = models.ManyToManyField(ActorModel, related_name= "films")
    
#     class Meta:
#         verbose_name = "Film"
    
#     def __str__(self) -> str:
#         return self.name



# # 3.2 modeller app-in admin.py-da qeyd olunur:
# from django.contrib import admin
# from film.models import ActorModel, FilmModel

# admin.site.register(ActorModel)
# admin.site.register(FilmModel)



# # 0.1 istifadeci(user) modeli ucun ayrica app yaradilir:
# from django.db import models
# from django.contrib.auth.models import User

# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to="accountphotos", blank=True, null=True)

#     def __str__(self):
#         return self.user.username


# # 0.2 account views.py:

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from account.models import Account
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.views import generic


# def has_num_alpha_symbol(t):
#     num = "0123456789"
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     symbol = "~!@#$%^&*()_+:|\\/?><.,"
#     x = False
#     y = False
#     z = False
#     for i in t:   
#         if i in num:
#             x = True 
#         if i in alpha:
#             y = True 
#         if i in symbol:
#             z = True
#         if x and y and z:
#                 break
#     if x and y and z:        
#         return True
#     else:
#         return False


# class RegisterView(generic.View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'register.html') # get metodda bi defe render yazmdimsa post metodda redirect istifade ede bileremde?
    
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get("username")
#         password = request.POST.get("password")

        
#         if username and password:
#             # if Account.objects.filter(user__username = username):
#             if User.objects.filter(username = username):    
#                 messages.info(request, "Please, enter another username")
#             # elif not has_num_alpha_symbol(password):
#             #     messages.info(request, "password must consist of letters and numbers")
#             elif password.isdigit():
#                 messages.info(request, "password must consist of letters and numbers")  
#             else:
#                 user = User.objects.create_user(username = username,password = password,)

#                 Account.objects.create(user = user,)
#                 messages.success(request, "User created")
#         print(3)        
#         print(username)
#         print(5)      
#         # if username is "":
#         if not username:
#             messages.info(request, "Please, enter username")
#         if not password:
#             messages.info(request, "Please, enter password")

#         return redirect("film:index")    
        

# # def register(request):
# #     if request.method == "POST":
# #         username = request.POST.get("username")
# #         password = request.POST.get("password")

        
# #         if username and password:
# #             if Account.objects.filter(user__username = username):
# #                 messages.info(request, "Please, enter another username")
# #             # elif not has_num_alpha_symbol(password):
# #             #     messages.info(request, "password must consist of letters and numbers")
# #             elif password.isdigit():
# #                 messages.info(request, "password must consist of letters and numbers")  
# #             else:
# #                 user = User.objects.create_user(username = username,password = password,)

# #                 Account.objects.create(user = user,)
# #                 messages.success(request, "User created")
# #         print(3)        
# #         print(username)
# #         print(5)      
# #         # if username is "":
# #         if not username:
# #             messages.info(request, "Please, enter username")
# #         if not password:
# #             messages.info(request, "Please, enter password")


                  

# #         # return redirect('film:index')

# #     return render(request, 'register.html')



# class LoginUserView(generic.View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'login.html')
    
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
        
#         user = authenticate(username = username, password = password)
#         print(user)
#         if user is None:
#             messages.info(request, "User was not found")

#         else:
#             login(request, user)
#             # return redirect("film:index")
#             messages.success(request, "%s login in." % (user.username))

#         return redirect("film:index")


# class LogoutUserView(generic.View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         messages.success(request,"Logging out")
#         return redirect("film:index")



# # def loginUser(request):
# #     if request.method == "POST":
# #         username = request.POST.get("username")
# #         password = request.POST.get("password")
        
# #         user = authenticate(username = username, password = password)
# #         print(user)
# #         if user is None:
# #             messages.info(request, "User was not found")

# #         else:
# #             login(request, user)
# #             # return redirect("film:index")
# #             messages.success(request, "%s login in." % (user.username))    

# #     return render(request, 'login.html')




# # 4. templates yaratdiqdan sonra adini proyektin settings.py-da:
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]





# # 6. media fayl yaradarken proyektin settings.py-da:

# """
# Django settings for filmpr project.

# Generated by 'django-admin startproject' using Django 4.1.5.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.1/ref/settings/
# """

# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-2nbyux1f2c4!m7%z%hq^y1&820@jv=r1=01=4s%@ztpepl%7e7'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'film',
#     'account',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'filmpr.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'filmpr.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Baku'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media'



# # 7. media fayl yaradarken proyektin urls.py-da:
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('film/', include('film.urls')),
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)