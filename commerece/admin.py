from django.contrib import admin

# Register your models here.
from .models import Album,Song,Test,Profile,Chat,Conversation,Contact
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Test)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Chat)
admin.site.register(Conversation)
