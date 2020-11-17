
from django.http import HttpResponse
from django.shortcuts import redirect

# Decorator for allowing Authenticated User only
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

# Decorator for Blocking Non-Admins from proceeding
def admin_user(view_fn):
    def wrapper_fn(request, *args, **kwargs):
        if request.user.is_admin or None:
            return view_fn(request, *args, **kwargs)
        else:
            HttpResponse("You are not allowed here")
    return wrapper_fn