from django import forms
from money_transfers.models import Transfer


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['payment', 'userfrom', 'userto', 'description', 'completed']
