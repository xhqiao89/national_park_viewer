from django.contrib.auth.decorators import login_required
from tethys_apps.sdk.gizmos import Button, TextInput, SelectInput
from django.shortcuts import render


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)

def map(request):

    btnSearch = Button(display_text="Generate Storage Capacity Curve",
                        name="btnSearch",
                        attributes="",
                        submit=False)

    damHeight = TextInput(display_text='Dam Height (m):',
                    name="damHeight",
                    initial="",
                    disabled=False,
                    attributes="")

    context = {'btnSearch': btnSearch,
               'damHeight': damHeight
               }

    return render(request, 'my_first_app/map.html', context)

def echo_name(request):
    """
    Controller that will echo the name provided by the user via a form.
    """
    # Default value for name
    name = ''

    # Define Gizmo Options
    text_input_options = TextInput(display_text='Enter Name',
                                   name='name-input')

    # Check form data
    if request.POST and 'name-input' in request.POST:
       name = request.POST['name-input']

    # Create template context dictionary
    context = {'name': name,
               'text_input_options': text_input_options}

    return render(request, 'my_first_app/echo_name.html', context)