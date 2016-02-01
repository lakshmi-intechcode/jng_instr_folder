Extending the Users Module, Again
=================================

In the final extension and refactor of your users module, we're going to add class based views and custom validations.

#### Set Up

Use the project with your most recent users app from the previous exercise.

#### Class Based Views

Take a look at the first three code snippets in [this Django doc](https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/)

This is how we would to it with a regular view function:
```py
def my_view(request):
	if request.method == 'GET':
		return render(request, 'helloword.html')
```
Here's how we do it with a class based view:
```py
from django.views.generic import View

class MyView(View):
	def get(self, request):
		return render(request, 'helloword.html')
	def post(self, request):
		return redirect('/success')
```
To use this in your `urls.py`, you'll need to import it.
```py
from myapp.views import MyView

urlpatterns = patterns('',
	(r'^helloword/', MyView.as_view()),
)
```
Take a look at the fourth code snippet in the linked doc above. Notice how you can keep variables in the class based view, like we could in any other class. We could store lots of stuff in there to DRY our code - like the template name, a ModelForm that you use on **GET** and **POST** routes, or really any other (immutable) data that both routes use.

#### Implement it

Refactor your users module to use only class based views. Take logical **GET** and **POST** routes and combine them.

#### Custom Validators

You've already used RegEx validator in the previous exercise. Now we want a custom validator. Using the [Validators Doc](https://docs.djangoproject.com/en/1.8/ref/validators/) write some custom validators on your Users model.

Passwords should be > 7 letters.
Username needs to be unique - also force this constraint on the database level.

On your POST route, make sure the `form.is_valid()`. If it is, save the form and redirect. If it is not, re-render on the same POST route page with an appropriate error.
