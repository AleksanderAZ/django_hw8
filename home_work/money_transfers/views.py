from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from money_transfers.models import Transfer
from money_transfers.forms import TransferForm
from money_transfers.mixins import (OwnerOnlyMixin, SuccessMessageMixin, QueryFilterMixin, 
                          TransferCounterMixin, RedirrectOnErrorMixin)

class TransferListView(LoginRequiredMixin, QueryFilterMixin, TransferCounterMixin, ListView):
    model = Transfer
    template_name = 'money_transfers/transfer_list.html'
    context_object_name = 'money_transfers'

    def get_queryset(self):
        money_transfers = super().get_queryset()
        if self.request.user.is_superuser:
            return money_transfers
        return money_transfers
        #return money_transfers.filter(userfrom=self.request.user)

class TransferCreateView(LoginRequiredMixin, SuccessMessageMixin, RedirrectOnErrorMixin, CreateView):
    model = Transfer
    form_class = TransferForm
    template_name = 'money_transfers/create_transfer.html'
    success_url = reverse_lazy('transfer_list')
    success_message = 'Перевід створений успішно!'
    error_redirect_url = reverse_lazy('transfer_list')

    def form_valid(self, form):
        form.instance.userfrom = self.request.user
        return super().form_valid(form)

class TransferDeleteView(LoginRequiredMixin, OwnerOnlyMixin, SuccessMessageMixin, DeleteView):
    model = Transfer
    template_name = 'money_transfers/confirm_delete.html'
    success_url = reverse_lazy('transfer_list')
    pk_url_kwarg = 'transfer_id'
    success_message = 'Видалено успішно!'
