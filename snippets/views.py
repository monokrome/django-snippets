from django.views.generic.list_detail import object_list,object_detail
from boundless.django.snippets.models import Snippet

RESULTS_PER_LIST_PAGE=100

def index(request, page=1):
    qs = Snippet.objects.all().order_by('-created_on')

    return object_list(request, queryset=qs, template_object_name='snippet',\
        paginate_by=RESULTS_PER_LIST_PAGE, page=page)

def snippet(request, identifier, slugified=False):
    data = {
        'queryset': Snippet.objects.all()
    }

    if slugified == False:
        data['object_id'] = identifier
    else:
        data['slug'] = identifier

    return object_detail(request, template_object_name='snippet', **data)

