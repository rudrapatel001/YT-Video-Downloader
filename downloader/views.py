from django.shortcuts import render, redirect
from .forms import YouTubeDownloadForm
from pytube import YouTube
from django.http import HttpResponse

def download_video(request):
    if request.method == 'POST':
        form = YouTubeDownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            try:
                yt = YouTube(video_url)
                yt.streams.first()  # Force prefetch stream
                video = yt.streams.get_highest_resolution()
                video.download()
                return HttpResponse(f"Video downloaded successfully: {yt.title}")
            except Exception as e:
                return HttpResponse(f"Error occurred: {e}")
    else:
        form = YouTubeDownloadForm()

    return render(request, 'downloader/index.html', {'form': form})
