from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django.forms import CheckboxInput
from . models import Tasks
from task_manager.labels.models import Labels


class TaskFilter(FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'self_tasks']

    def __init__(self, *args, **kwargs):
        super(TaskFilter, self).__init__(*args, **kwargs)
        self.filters['status'].label = 'Статус'
        self.filters['executor'].label = 'Исполнитель'

    label = ModelChoiceFilter(
        field_name='labels',
        label="Метка",
        queryset=Labels.objects.all())

    def logined_user_is_creator_filter(self, queryset, name, value):
        user = self.request.user
        if value:
            return queryset.filter(author=user)
        return queryset

    self_tasks = BooleanFilter(
        field_name="author",
        method='logined_user_is_creator_filter',
        label="Только свои задачи",
        widget=CheckboxInput(attrs={'checked': False}))
