from django import forms

class YouTubeDownloadForm(forms.Form):
    video_url = forms.URLField(label='YouTube Video URL', max_length=200)
