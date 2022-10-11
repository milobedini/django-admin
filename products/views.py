from rest_framework import viewsets


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        pass

    def create(self, request):
        pass

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
