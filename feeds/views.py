from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Feed
from .forms import FeedForm

@login_required(login_url='/accounts/login/')
def feed_list(request):
    """Handle both displaying and creating feed posts"""
    feeds = Feed.objects.all().order_by('-created_at')  # Newest first
    
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            new_feed = form.save(commit=False)
            new_feed.user = request.user
            new_feed.save()
            return redirect('feeds:feed_list')
    else:
        form = FeedForm()
    
    return render(request, 'feeds/feed_list.html', {
        'form': form,
        'feeds': feeds
    })

@login_required
def delete_feed(request, pk):
    """Handle feed post deletion with confirmation"""
    feed = get_object_or_404(Feed, pk=pk, user=request.user)
    
    if request.method == 'POST':
        feed.delete()
        return redirect('feeds:feed_list')
    
    return render(request, 'feeds/confirm_delete.html', {'feed': feed})

@login_required
@require_POST
def like_feed(request, pk):
    """Handle like/unlike actions via AJAX"""
    feed = get_object_or_404(Feed, pk=pk)
    user = request.user
    
    if user in feed.likes.all():
        feed.likes.remove(user)
        liked = False
    else:
        feed.likes.add(user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'count': feed.likes.count(),
        'feed_id': feed.pk
    })