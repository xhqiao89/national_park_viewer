from tethys_sdk.base import TethysAppBase, url_map_maker

class MyFirstApp(TethysAppBase):
    """
    Tethys app class for My First App.
    """

    name = 'US National Parks Adventure'
    index = 'my_first_app:home'
    icon = 'my_first_app/images/icon_f.png'
    package = 'my_first_app'
    root_url = 'my-first-app'
    color = '#38610B'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-first-app',
                           controller='my_first_app.controllers.home'),
                    UrlMap(name='map',
                           url='my-first-app/map',
                           controller='my_first_app.controllers.map'),
                    UrlMap(name='echo_name',
                           url='my-first-app/echo-name',
                           controller='my_first_app.controllers.echo_name'),
        )

        return url_maps