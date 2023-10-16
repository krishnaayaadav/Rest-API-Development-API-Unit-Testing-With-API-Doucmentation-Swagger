from rest_framework.pagination import PageNumberPagination

class ExpensePagination(PageNumberPagination):
    """Custom Pagination for expense pagination"""
    
    page_size = 1
    page_size_query_param = 'page_size'
    max_page  = 1000

