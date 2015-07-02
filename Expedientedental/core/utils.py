import re

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):

    return [normspace(' ',
            (t[0] or t[1]).strip()) for t in findterms(query_string)]


def build_query(query_string, search_fields):
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{'%s__icontains' % field_name: term})

            if or_query:
                or_query = or_query | q
            else:
                or_query = q

        if query:
            query = query & or_query
        else:
            query = or_query
    return query


def generic_search(request, model, fields, query_param='q'):

    query_string = request.GET.get(query_param, '').strip()

    if not query_string:
        return model.objects.all()

    entry_query = build_query(query_string, fields)

    found_entries = model.objects.filter(entry_query)

    return found_entries


def paginate_objects(request, queryset, num_items):
    paginator = Paginator(queryset, num_items)
    page = request.GET.get('page') or 1
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page, page.object_list, page.has_other_pages()
