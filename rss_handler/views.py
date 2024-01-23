from django.contrib.auth import authenticate, login
from django.contrib import messages

from rss_handler.forms import *

from django.contrib.auth.decorators import login_required
from .models import RSSFeed
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('manage_rss_feeds')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('manage_rss_feeds')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'admin/login.html')


@login_required(login_url='admin_login')
def dashboard(request):
    return render(request, './manage_rss_feeds.html')


@login_required(login_url='admin_login')
def dashboard(request):
    rss_feeds = RSSFeed.objects.all()
    rss_feed_form = RSSFeedForm(request.POST or None)
    gpt_prompt_form = GPTPromptSettingsForm(request.POST or None)
    google_chat_form = GoogleChatSettingsForm(request.POST or None)
    telegram_form = TelegramSettingsForm(request.POST or None)
    fibery_crm_form = FiberyCRMSettingsForm(request.POST or None)

    if request.method == 'POST':
        if rss_feed_form.is_valid():
            rss_feed_form.save()
            messages.success(request, 'RSS Feed saved successfully!')
        if gpt_prompt_form.is_valid():
            gpt_prompt_form.save()
            messages.success(request, 'GPT Prompt Setting saved successfully!')
        if google_chat_form.is_valid():
            google_chat_form.save()
            messages.success(request, 'Google Chat Setting saved successfully!')
        if telegram_form.is_valid():
            telegram_form.save()
            messages.success(request, 'Telegram Setting saved successfully!')
        if fibery_crm_form.is_valid():
            fibery_crm_form.save()
            messages.success(request, 'Fibery CRM Setting saved successfully!')

        return redirect('manage_rss_feeds')

    context = {
        'rss_feed_form': rss_feed_form,
        'gpt_prompt_form': gpt_prompt_form,
        'google_chat_form': google_chat_form,
        'telegram_form': telegram_form,
        'fibery_crm_form': fibery_crm_form,
        'rss_feeds': rss_feeds,
    }

    return render(request, 'admin/dashboard.html', context)


@login_required
def manage_rss_feeds(request):
    rss_feeds = RSSFeed.objects.all()
    return render(request, 'manage_rss_feeds.html', {'rss_feeds': rss_feeds})


@require_POST
@login_required
def toggle_rss_feed_status(request, pk):
    rss_feed = get_object_or_404(RSSFeed, pk=pk)
    rss_feed.is_enabled = not rss_feed.is_enabled
    rss_feed.save()
    messages.success(request, f"RSS feed {'activated' if rss_feed.is_enabled else 'deactivated'} successfully.")
    return redirect('manage_rss_feeds')


@require_POST
@login_required
def delete_rss_feed(request, pk):
    rss_feed = get_object_or_404(RSSFeed, pk=pk)
    rss_feed.delete()
    messages.success(request, "RSS feed deleted successfully.")
    return redirect('manage_rss_feeds')



