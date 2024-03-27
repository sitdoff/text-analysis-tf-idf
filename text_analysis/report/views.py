from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from .report_servises import CreateReport


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Returns a template with a file upload form or analysis results.

    GET: render template with form
    POST: render template with result
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            report_creator = CreateReport(request.FILES["file"])
            report = report_creator.create_report()
            return render(request, "report/show_report.html", context={"report": report})
    else:
        form = UploadFileForm()
    return render(request, "report/upload_file.html", {"form": form})
