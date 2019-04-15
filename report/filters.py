from material_transaction.models import Purchase
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = ['rawitem']