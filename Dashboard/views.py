from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from Item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    context = {
        'products': items,
    }

    return render(request, 'dashboard/index.html', context)
