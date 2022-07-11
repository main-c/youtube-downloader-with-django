from pprint import pprint
from django.shortcuts import redirect, render
from django.views import View
from pytube import YouTube
from core.forms import Downloadform


class DownloadView(View):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        form = Downloadform()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = Downloadform(data=request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("yt_link")
            print(url)
            yt = YouTube(url).streams.filter().order_by("resolution")
            pprint(yt)
            return render(request, self.template_name, {'file':yt})

        else:
            return render(request, self.template_name, {"form": form})
