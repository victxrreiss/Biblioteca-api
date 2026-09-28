# TODO: implementação pendente — responsabilidade de outro integrante do grupo.

from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet

router = DefaultRouter()

router.register(
    r"autores",
    AutorViewSet,
    basename="autor"
)

router.register(
    r"livros",
    LivroViewSet,
    basename="livro"
)

urlpatterns = router.urls