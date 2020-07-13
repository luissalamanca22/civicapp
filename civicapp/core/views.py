from django.shortcuts import render
from django.views.generic.edit import FormView

from core.models import Profile
from core.forms import ProfileForm

# Create your views here.
class ProfileView(FormView):
    """Update view for profile"""
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/form.html'

    # def get_initial(self):
    #     """Return the initial data to use for forms on this view."""
    #     return {"aceptedPP": True}

    def get_token(self):
        return self.request.GET.get("token", None)

    def get_object(self):
        token = self.get_token()
        try:
            decoded = jwt.decode(token, 'secret')
            print(decoded)
            print("-"*100)
            return Appointment.objects.get(id=decoded["id"])
        except:
            return None

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = self.get_object()
    #     context['token'] = self.get_token()
    #     #context['BASE_SITE_URL'] = settings.BASE_SITE_URL
    #     return context

    def get_success_url(self):
        return "/citas/helper/?token=%s" % self.get_token()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        form.instance = self.get_object()
        #form.instance.ip_actualizacion = "hola"
        # print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)