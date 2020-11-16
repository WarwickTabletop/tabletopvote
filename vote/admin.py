from django.contrib import admin

from .models import Election, Option, Vote


class OptionInlineEdit(admin.StackedInline):
    model = Option
    readonly_fields = ['votes']
    extra = 0


class OptionInlineCreate(admin.StackedInline):
    model = Option
    readonly_fields = ['votes']
    extra = 1


class ElectionAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = [OptionInlineEdit]
        return super().change_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = [OptionInlineCreate]
        return super().add_view(request, form_url, extra_context)


class VoteAdmin(admin.ModelAdmin):
    readonly_fields = ['ip', 'uuid', 'time', 'election', 'selections']


# Register your models here.
admin.site.register(Election, ElectionAdmin)
admin.site.register(Vote, VoteAdmin)
