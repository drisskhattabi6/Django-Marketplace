from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from Item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            conversation_id = conversation.id

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:detail', pk=conversation_id)
    else:
        form = ConversationMessageForm()
    
    context = {
        'form': form
    }
    return render(request, 'conversation/new.html', context)


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    context = {
        'conversations': conversations
    }

    return render(request, 'conversation/inbox.html', context)


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    print("pk :", pk)

    if request.method == 'POST':
        # message_content = request.POST.get('content')
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()
            
    else:
        form = ConversationMessageForm()

    context = {
        'conversation': conversation,
        'form': form
    }

    return render(request, 'conversation/detail.html', context)
