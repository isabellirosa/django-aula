from django.contrib import admin
from .models import Formacao
from .models import Instituicao
from .models import Instrutor
# Register your models here.
admin.site.register(Formacao)
admin.site.register(Instituicao)
admin.site.register(Instrutor)