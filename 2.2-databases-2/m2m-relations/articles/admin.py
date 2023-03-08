from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if dictionary.get('is_main'):
                i += 1
            else:
                continue
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

