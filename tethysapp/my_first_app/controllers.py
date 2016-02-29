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

    btnSearch = Button(display_text="Zoom in",
                        name="btnSearch",
                        attributes="",
                        submit=False)

    stateSelect = SelectInput(display_text="Select a state:",
                                name='stateSelect',
                                multiple=False,
                                options=[('Alaska', 'AK'), ('American Samoa','AS'), ('Arizona', 'AZ'), ('Arkansas', 'AR'),
                                         ('California', 'CA'), ('Colorado', 'CO'), ('Florida', 'FL'), ('Colorado', 'CO'),
                                         ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Kentucky', 'KY'), ('Maine', 'ME'), ('Michigan', 'MI'),
                                         ('Hawaii', 'HI'),('Minnesota', 'MN'),('Montana', 'MT'), ('Nevada', 'NV'), ('New Mexico', 'NM'),
                                         ('North Dakota', 'ND'), ('Ohio', 'OH'), ('Oregon', 'OR'), ('South Dakota', 'SD'), ('Tennessee', 'TN'),
                                         ('Texas', 'TX'), ('Virgin Islands', 'VI'), ('Utah', 'UT'), ('Washington', 'WA'), ('Wyoming', 'WY') ],
                                original='',
                                attributes="id=select_state onchange=select_state();")

    stateSelect = SelectInput(display_text="Select a state:",
                                name='stateSelect',
                                multiple=False,
                                options=[('Alaska', 'AK'), ('American Samoa','AS'), ('Arizona', 'AZ'), ('Arkansas', 'AR'),
                                         ('California', 'CA'), ('Colorado', 'CO'), ('Florida', 'FL'), ('Colorado', 'CO'),
                                         ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Kentucky', 'KY'), ('Maine', 'ME'), ('Michigan', 'MI'),
                                         ('Hawaii', 'HI'),('Minnesota', 'MN'),('Montana', 'MT'), ('Nevada', 'NV'), ('New Mexico', 'NM'),
                                         ('North Dakota', 'ND'), ('Ohio', 'OH'), ('Oregon', 'OR'), ('South Dakota', 'SD'), ('Tennessee', 'TN'),
                                         ('Texas', 'TX'), ('Virgin Islands', 'VI'), ('Utah', 'UT'), ('Washington', 'WA'), ('Wyoming', 'WY') ],
                                original='',
                                attributes="id=select_state onchange=select_state();")


    context = {'btnSearch': btnSearch,
               'stateSelect': stateSelect
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