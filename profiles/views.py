from django.contrib.auth.models import User
from django.views.generic import DetailView, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest

from feed.models import Post
from followers.models import Follower
from . models import Profile
from . forms import UpdateForm


class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        context['total_followers'] = Follower.objects.filter(
            following=user).count()
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(
                following=user, followed_by=self.request.user).exists()
        return context

# simple, hardcoded view for profile update
# follow one of the tutorials on this one; still geting NoReverseMatch with profile_update


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UpdateForm
    template_name = "profiles/update.html"
    success_url = '/'
    context_object_name = "update"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.profile
        return context


class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing Data")

        try:
            other_user = User.objects.get(username=data['username'])

        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing User")

        if data['action'] == "follow":
            # Follow
            print(other_user)
            follower, created = Follower.objects.get_or_create(
                followed_by=request.user,
                following=other_user
            )
        else:
            # Unfollow
            try:
                follower = Follower.objects.get(
                    followed_by=request.user,
                    following=other_user
                )

            except Follower.DoesNotExist:
                follower = None

            if follower:
                follower.delete()

        return JsonResponse({
            'success': True,
            'wording': "Unfollow" if data['action'] == "follow" else "Follow"
        })
