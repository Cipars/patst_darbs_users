from django.shortcuts import render
from django.views.generic import ListView, View, FormView
from user.models import User
from user.forms import UserForm


class DeleteUserView(View):

    def get(self, request, user_id):

        user = User.objects.get(id=user_id)

        context = {
            'name': user.name
        }

        User.objects.filter(id=user_id).delete()

        return render(
            template_name='delete_user.html',
            request=request,
            context=context,
        )


class EditUserView(View):

    def get(self, request, user_id):

        return render(
            template_name='edit_user.html',
            request=request,
            context={},
        )

    def post(self, request, user_id):

        user = User(
            name=request.POST['name'],
            email=request.POST['email'],
        )

        User.objects.filter(id=user_id).update(
            name=user.name,
            email=user.email,
        )

        context = {
            'name': user.name,
            'email': user.email,
        }

        return render(
            template_name='user_detail.html',
            request=request,
            context=context,
        )


class UserListView(ListView):

    model = User
    template_name = 'user_list.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):

        form.save()
        response = super().form_valid(form)

        return response
