from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, get_list_or_404, render
from pressbox.models import PressItem

def press_list(request, template_name='pressbox/object_list.html', extra_context={}):
    return render(request,template_name, extra_context)

def press_regroup(request, template_name='pressbox/object_list_by_category.html', extra_context={}):
    return render(request,template_name, extra_context)

def press_with_templatetag(request, template_name='pressbox/object_list_by_category_tag.html', extra_context={}):
    return render(request,template_name, extra_context)

def press_detail(request, slug, template_name='pressbox/object_detail.html'):
    extra_context['object'] = PressItem.objects.active().get(slug=slug)
    return render(request,template_name, extra_context)
