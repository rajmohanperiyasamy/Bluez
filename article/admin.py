from django.contrib import admin
from article.models import ClientsData
from article.models import Accounts
from article.models import Clients
from article.models import Document
admin.site.register(Accounts)
admin.site.register(Clients)
admin.site.register(Document)
admin.site.register(ClientsData)
# Register your models here.