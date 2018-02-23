from django.shortcuts import render
from blockchain.models import Block


def index(request):
    context = {'blocks': Block.objects.all(), 'just_test': 'Hello World!'}
    return render(request, 'blockchain/index.html', context)
