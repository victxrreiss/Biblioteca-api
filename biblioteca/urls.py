# TODO: implementação pendente — responsabilidade de outro integrante do grupo.

from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet, AutorResumoViewSet, LivroResumoViewSet

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

router.register(
    r"autores_r",
    AutorResumoViewSet,
    basename="autor_r"
)

router.register(
    r"livros_r",
    LivroResumoViewSet,
    basename="livro_r"
)

urlpatterns = router.urls