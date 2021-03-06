from django.conf.urls import patterns, url
from views import ResetPasswordRequestView, PasswordResetConfirmView

urlpatterns = patterns('',
    url(r'^register$', 'accounts.views.register', name='register'),
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),
    url(r'^profilepage$', 'accounts.views.profilepage', name='profile'),
    url(r'^feedbackpage$', 'accounts.views.feedbackpage', name='feedback'),

    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    # PS: url above is going to used for next section of implementation.
    url(r'^reset_password$', ResetPasswordRequestView.as_view(), name="reset_password"),
    url(r'^request_account_retrieval$', 'accounts.views.request_account_retrieval', name='request_account_retrieval'),

)
