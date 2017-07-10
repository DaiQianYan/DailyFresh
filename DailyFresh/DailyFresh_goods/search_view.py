from haystack.generic_views import SearchView

class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['cart_show'] = '1'
        return context

    
