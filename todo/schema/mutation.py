import graphene
from .types import TodoItemType
from ..models import TodoItem

class CreateTodoItem(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    todo_item = graphene.Field(TodoItemType)

    def mutate(self, info, title):
        todo_item = TodoItem.objects.create(title=title)
        return CreateTodoItem(todo_item=todo_item)

class UpdateTodoItem(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        completed = graphene.Boolean()

    todo_item = graphene.Field(TodoItemType)

    def mutate(self, info, id, title=None, completed=None):
        todo_item = TodoItem.objects.get(pk=id)
        if title is not None:
            todo_item.title = title
        if completed is not None:
            todo_item.completed = completed
        todo_item.save()
        return UpdateTodoItem(todo_item=todo_item)

class DeleteTodoItem(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        TodoItem.objects.get(pk=id).delete()
        return DeleteTodoItem(success=True)

class Mutation(graphene.ObjectType):
    create_todo_item = CreateTodoItem.Field()
    update_todo_item = UpdateTodoItem.Field()
    delete_todo_item = DeleteTodoItem.Field()
