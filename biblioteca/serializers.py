from datetime import date

from rest_framework import serializers

from .models import Autor, Livro


class AutorResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ["id", "nome"]


class LivroResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "ano_publicacao"]


class AutorSerializer(serializers.ModelSerializer):
    livros = LivroResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ["id", "nome", "nacionalidade", "data_nascimento", "livros"]


class LivroSerializer(serializers.ModelSerializer):
    autor = AutorResumoSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(
        source="autor", queryset=Autor.objects.all(), write_only=True
    )

    class Meta:
        model = Livro
        fields = ["id", "titulo", "isbn", "ano_publicacao", "genero", "autor", "autor_id"]

    def validate_ano_publicacao(self, value):
        if value > date.today().year:
            raise serializers.ValidationError(
                "O ano de publicação não pode ser maior que o ano atual."
            )
        return value
