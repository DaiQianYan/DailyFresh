from haystack.generic_views import SearchView


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
    	# 定义context
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # 调试
        # print(context)

        context['cart_show'] = '1'
        # 将索引的页码判断写在视图里
        # 创建一个储存页码的列表
        page_list = []
        page_obj = context['page_obj']


        if page_obj.paginator.num_pages < 5:
        	page_list = range(1, page_obj.paginator.num_pages+1)
        elif page_obj.number <= 2:
        	page_list = range(1, 5+1)
        elif page_obj.number >= page_obj.paginator.num_pages-1:
        	page_list = range(page_obj.paginator.num_pages-5+1, page_obj.paginator.num_pages+1)
        else:
        	page_list = range(page_obj.number-2, page_obj.number+3)

        context['page_list'] = page_list
        return context