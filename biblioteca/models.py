from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=80, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nome


class Livro(models.Model):
    class Genero(models.TextChoices):
        FICCAO = "FICCAO", "Ficção"
        ROMANCE = "ROMANCE", "Romance"
        TECNICO = "TECNICO", "Técnico"
        BIOGRAFIA = "BIOGRAFIA", "Biografia"
        FANTASIA = "FANTASIA", "Fantasia"

    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.PositiveIntegerField()
    genero = models.CharField(max_length=30, choices=Genero.choices)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.titulo
