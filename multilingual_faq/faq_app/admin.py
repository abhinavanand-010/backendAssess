from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_translated_question_hi', 'get_translated_question_bn')

    def get_translated_question_hi(self, obj):
        return obj.question_hi
    get_translated_question_hi.short_description = 'Hindi Question'

    def get_translated_question_bn(self, obj):
        return obj.question_bn
    get_translated_question_bn.short_description = 'Bengali Question'