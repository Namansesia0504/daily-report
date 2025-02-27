from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import Tweetform  # Ensure this is correctly named

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)  # Save but don't commit yet
            tweet.user = request.user  # Assign the current user to the tweet
            tweet.save()
            return redirect('tweet_list')  # Redirect to the tweet list page
    else:
        form = Tweetform()  # Initialize an empty form for GET request
    
    return render(request, 'tweet_form.html', {'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure only the user who created it can edit
    
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Ensure the tweet is associated with the correct user
            tweet.save()
            return redirect('tweet_list')  # After saving, redirect to the tweet list page
    else:
        form = Tweetform(instance=tweet)  # Populate the form with existing tweet data
    
    return render(request, 'tweet_form.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')  # Redirect to the tweet list after deletion
    
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  # Confirm deletion page




