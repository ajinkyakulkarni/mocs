# Create your views here.
from lib.database import Author, Conference, Journal
from utils import json_response, generalize

def to_val_list(named_tpls, name_lookup_fn, doc_lookup_fn = lambda t: t.doc_count):
    return [{'label': '%s : %d' % (name_lookup_fn(named_tpl), doc_lookup_fn(named_tpl)),
             'value': name_lookup_fn(named_tpl)}
            for named_tpl in named_tpls]

@json_response
def top_authors(request):
    if request.method == 'GET':
        term = request.GET.get('term')
        n = request.GET.get('n', 10)
        print 'getting %d authors for %s' % (n, term)
        entities_and_counts = Author.name_like_top(generalize(term), n=n)
        val_list = to_val_list(entities_and_counts, name_lookup_fn=lambda t: t.Author.name)
        print '%d entities found' % (len(val_list))
        return val_list

@json_response
def top_journals(request):
    if request.method == 'GET':
        term = request.GET.get('term')
        n = request.GET.get('n', 10)
        print 'getting %d journals for %s' % (n, term)
        entities_and_counts = Journal.name_like_top(generalize(term), n=n)
        val_list = to_val_list(entities_and_counts, name_lookup_fn=lambda t: t.Journal.name)
        print '%d entities found' % (len(val_list))
        return val_list

@json_response
def top_conferences(request):
    if request.method == 'GET':
        term = request.GET.get('term')
        n = request.GET.get('n', 10)
        print 'getting %d conferences for %s' % (n, term)
        entities_and_counts = Conference.name_like_top(generalize(term), n=n)
        val_list = to_val_list(entities_and_counts, name_lookup_fn=lambda t: t.Conference.name)
        print '%d entities found' % (len(val_list))
        return val_list