from tethys_apps.sdk.gizmos import Button, TextInput, SelectInput, RangeSlider
from django.shortcuts import render


def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)

def map(request):

    select_park = SelectInput(display_text="Select a park:",
                                name='select_park',
                                multiple=False,
                                options=[('Acadia,Maine', 'Acadia'), ('American Samoa,American Samoa','American Samoa'), ('Arches,Utah', 'Arches'), ('Badlands,South Dakota', 'Badlands'),
                                         ('Big Bend,Texas', 'Big Bend'), ('Biscayne,Florida', 'Biscayne'), ('Black Canyon of the Gunnison,Colorado', 'Black Canyon of the Gunnison'), ('Bryce Canyon,Utah', 'Bryce Canyon'),
                                         ('Canyonlands,Utah', 'Canyonlands'), ('Capitol Reef,Utah', 'Capitol Reef'), ('Carlsbad Caverns,New Mexico', 'Carlsbad Caverns'), ('Channel Islands,California', 'Channel Islands'), ('Congaree,South Carolina', 'Congaree'),
                                         ('Crater Lake,Oregon', 'Crater Lake'),('Cuyahoga Valley,Ohio', 'Cuyahoga Valley'),('Death Valley,California', 'Death Valley'), ('Denali,Alaska', 'Denali'), ('Dry Tortugas,Florida', 'Dry Tortugas'),
                                         ('Everglades,Florida', 'Everglades'), ('Gates of the Arctic,Alaska', 'Gates of the Arctic'), ('Glacier,Montana', 'Glacier'), ('Glacier Bay,Alaska', 'Glacier Bay'), ('Grand Canyon,Arizona', 'Grand Canyon'),
                                         ('Grand Teton,Wyoming', 'Grand Teton'), ('Great Basin,Nevada', 'Great Basin'), ('Great Sand Dunes,Colorado', 'Great Sand Dunes'), ('Great Smoky Mountains,North Carolina', 'Great Smoky Mountains'), ('Guadalupe Mountains,Texas', 'Guadalupe Mountains'),
                                         ('Haleakala,Hawaii', 'Haleakala'), ('Hawaii Volcanoes,Hawaii', 'Hawaii Volcanoes'), ('Hot Springs,Arkansas', 'Hot Springs'), ('Isle Royale,Michigan', 'Isle Royale'), ('Isle Royale,Michigan', 'Isle Royale'),
                                         ('Joshua Tree,California', 'Joshua Tree'), ('Katmai,Alaska', 'Katmai'), ('Kenai Fjords,Alaska', 'Kenai Fjords'), ('Kings Canyon,California', 'Kings Canyon'), ('Kobuk Valley,Alaska', 'Kobuk Valley'),
                                         ('Lake Clark,Alaska', 'Lake Clark'), ('Lassen Volcanic,California', 'Lassen Volcanic'), ('Mammoth Cave,Kentucky', 'Mammoth Cave'), ('Mesa Verde,Colorado', 'Mesa Verde'), ('Mount Rainier,Washington', 'Mount Rainier'),
                                         ('North Cascades,Washington', 'North Cascades'), ('Olympic,Washington', 'Olympic'), ('Petrified Forest,Arizona', 'Petrified Forest'), ('Pinnacles,California', 'Pinnacles'), ('Redwood,California', 'Redwood'),
                                         ('Rocky Mountain,Colorado', 'Rocky Mountain'), ('Saguaro,Arizona', 'Saguaro'), ('Sequoia,California', 'Sequoia'), ('Shenandoah,Virginia', 'Shenandoah'), ('Theodore Roosevelt,North Dakota', 'Theodore Roosevelt'),
                                         ('Virgin Islands,Virgin Islands', 'Virgin Islands'), ('Voyageurs,Minnesota', 'Voyageurs'), ('Wind Cave,South Dakota', 'Wind Cave'), ('Wrangell-St. Elias,Alaska', 'Wrangell-St. Elias'), ('Yellowstone,Wyoming', 'Yellowstone'),
                                         ('Yosemite,California', 'Yosemite'), ('Zion,Utah', 'Zion')],
                                original='',
                                attributes="id=select_state onchange=select_park();")
    slider1 = RangeSlider(display_text='Slider 1',
                      name='slider1',
                      min=1872,
                      max=2004,
                      initial=1,
                      step=1)


    context = {'select_park': select_park,
               'slider1': slider1
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