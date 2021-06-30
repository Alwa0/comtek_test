from datetime import datetime
from django.http import HttpResponse
from api.models import *
from django.core.paginator import Paginator
from django.shortcuts import render


# method that allows get a list of catalogs
def catalogs(request):
    dirs_list = Catalog.objects.all()
    paginator = Paginator(dirs_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogs.html', {'page_obj': page_obj})


# method that allows get a list of catalogs relevant as of the specified date
def catalogs_date(request, year, month, day):
    st = f"{year}-{month}-{day}"
    try:
        d = datetime.strptime(st, "%Y-%m-%d")
    except ValueError:
        return HttpResponse("Please, use date in 'yyyy-mm-dd' format")

    catalogs_list = Catalog.objects.filter(start_date__gte=d)
    if len(catalogs_list) == 0:
        return HttpResponse("There are no catalogs matching your search")

    paginator = Paginator(catalogs_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogs.html', {'page_obj': page_obj})


# method that allows get elements of the specific catalog(by current version or specific one)
def get_elements(request, fullname, version=None):
    # if current version is required
    if version is None:
        catalog_list = Catalog.objects.filter(fullname=fullname)
        if len(catalog_list) > 0:
            catalog = catalog_list.latest("start_date")
        else:
            return HttpResponse("There is no catalog matching your search")

    # if specific version is required
    else:
        catalog_list = Catalog.objects.filter(fullname=fullname, version=version)
        if len(catalog_list) == 0:
            return HttpResponse("There is no catalog matching your search")
        else:
            catalog = catalog_list[0]

    elements_list = Element.objects.filter(catalog=catalog)
    paginator = Paginator(elements_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'elements.html', {'page_obj': page_obj})


