import graphene
from graphene_django.types import DjangoObjectType
from ..models import TodoItem

class TodoItemType(DjangoObjectType):
    class Meta:
        model = TodoItem