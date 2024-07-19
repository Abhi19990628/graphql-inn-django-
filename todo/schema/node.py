import graphene
from graphene.relay import Node
from graphene_django.types import DjangoObjectType
from ..models import TodoItem

class TodoItemNode(DjangoObjectType):
    class Meta:
        model = TodoItem
        interfaces = (Node,)
