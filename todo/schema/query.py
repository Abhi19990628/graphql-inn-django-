import graphene
from .types import TodoItemType
from ..models import TodoItem

class Query(graphene.ObjectType):
    todo_items = graphene.List(TodoItemType)
    todo_item = graphene.Field(TodoItemType, id=graphene.Int(required=True))

    def resolve_todo_items(self, info):
        return TodoItem.objects.all()

    def resolve_todo_item(self, info, id):
        return TodoItem.objects.get(pk=id)
