from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer


class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = []

        for faq in faqs:
            translated_question = faq.get_translated_question(lang)
            translated_answer = faq.get_translated_answer(lang)
            data.append({
                'id': faq.id,
                'question': translated_question,
                'answer': translated_answer,
            })

        cache.set(cache_key, data, timeout=3600)
        return Response(data)