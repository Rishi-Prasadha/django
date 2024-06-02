# Weather Widget
### 6/2/2024

### Things Learned

* The HTML file (frontend) and the methods in views.py (backend) are connected to each other via the render function:
`return render(request, 'main/index.html', data)`
Where Django knows to replace the template values (e.g. {{temp}}) in main/index.html with that in data through dictionary comprehension

* If `APP_DIRS: True` in settings.py that means Django will automatically search for a templates folder, hence no need to write `templates/main/index.html`

* a `request.POST` object contains the data that the user inputted as a dictionary and is accessed by the backend for anything to happen

* In a Django project, import your environment variables in settings.py:
`load_dotenv(os.path.join(BASE_DIR, '.env'))`

* a `{% csrf_token%}` stands for Cross-Site Request Forgery, and Django requires that all POST requests include a CSRF token. This is to prevent malicious attacks from happening by taking advantage of a user's active session. Best practices on where to put the token are:

**After the `<form>` tag**
```
<form method="post">
	{% csrf_token %}
</form>
```

**Before the submit button**
```
<form method="post">
	<!-- form fields go here -->
	{% csrf_token %}
	<button type="submit">Submit</button>
</form>
```


