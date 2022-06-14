from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile

from archive.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from archive.models import Pic
from archive.forms import CreateForm


class PicListView(OwnerListView):
    model = Pic
    template_name = "archive/list.html"


class PicDetailView(OwnerDetailView):
    model = Pic
    template_name = "archive/detail.html"


class PicCreateView(LoginRequiredMixin, View):                      #views.py works as a controller,
    template_name = 'archive/form.html'                                   # talking to the browser, through forms
    success_url = reverse_lazy('archive:oilpainting')                             # interacting with the database, through models

    def get(self, request, pk=None): #get the form first, building the form includimg ['title', 'text', 'picture'] fields
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):                               #working with the form
        form = CreateForm(request.POST, request.FILES or None)            #constructing the form first

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving                       #working with the model
        pic = form.save(commit=False)                                   #get me the model, but don't store in the database
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class PicUpdateView(LoginRequiredMixin, View):
    template_name = 'archive/form.html'
    success_url = reverse_lazy('archive:oilpainting')

    def get(self, request, pk):
        pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Pic, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class PicDeleteView(OwnerDeleteView):
    model = Pic
    template_name = "archive/delete.html"


def stream_file(request, pk):
    pic = get_object_or_404(Pic, id=pk)
    response = HttpResponse()          #html respose
    response['Content-Type'] = pic.content_type #not text, but image/png shown in HEADER
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)     #write the pixels
    return response
