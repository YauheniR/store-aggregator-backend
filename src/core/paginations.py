from rest_framework.pagination import CursorPagination


class StandardResultsSetPagination(CursorPagination):
    page_size = 10
