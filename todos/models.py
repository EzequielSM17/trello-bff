from django.db import models
from users.models import User

# Create your models here.


class ToDoTypes(models.Model):
    """ Model del tipo de tareas """
    LOWER = "LO"
    MEDIUM = "ME"
    HIGH = "HI"
    URGENT = "UR"
    PRIORITY_TYPES = {
        LOWER: "Lower",
        MEDIUM: "Medium",
        HIGH: "High",
        URGENT: "Urgent",
    }
    name = models.CharField('Título', max_length=32)
    priority = models.CharField('Prioridad', max_length=2,
                                choices=PRIORITY_TYPES,
                                default=LOWER,
                                )

    class Meta:
        verbose_name = 'Tipo de tareas'
        verbose_name_plural = 'Tipos de tareas'

    def __str__(self):
        return f'{self.name}'


class ToDoState(models.Model):
    """ Model del tipo de tareas "To Do", "In progress", "Waiting", "Done" """
    TODO = "To Do"
    IN_PROGRESS = "In progress"
    WAITING = "Waiting"
    DONE = "Done"
    STATES = {
        TODO: "To Do",
        IN_PROGRESS: "In progress",
        WAITING: "Waiting",
        DONE:  "Done",
    }
    name = models.CharField('Prioridad', max_length=12,
                            choices=STATES,
                            default=TODO,
                            )

    class Meta:
        verbose_name = 'Estado de tarea'
        verbose_name_plural = 'Estados de tareas'

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    """ Model de las tareas """
    title = models.CharField('Título', max_length=32)
    description = models.CharField('Description', max_length=200)
    date = models.DateField(
        'Día de la creación de la tarea', auto_now=False, auto_now_add=True, null=True, blank=True)
    deadline = models.DateField(
        'Día de entrega de la tarea', auto_now=False, auto_now_add=False, null=False, blank=False)
    type = models.ForeignKey(ToDoTypes, on_delete=models.PROTECT)
    state = models.ForeignKey(ToDoState, on_delete=models.PROTECT)
    people = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return f'{self.title}'
