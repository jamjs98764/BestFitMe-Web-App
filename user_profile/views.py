from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect


#require user login ** 
@login_required
def display(request):
	return render(request, "user_profile/main.html")




