from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields' : ['questionText']},),
    ('Date information', {'fields' : ['pubDate'], 'classes' : ['collapse']}), 
  ]
  inlines = [ChoiceInline]
  list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
  list_filter = ['pubDate']

# Register your models here.
admin.site.register(Question, QuestionAdmin)