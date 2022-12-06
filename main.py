# Project Hakkonen by Alex Arbuckle #


# import <
import dash_bootstrap_components as dbc

from frontend.feed import feedFunction
from backend.resource import application
from frontend.project import projectFunction

# >


application.layout = dbc.Container(

    fluid = True,
    style = dict(backgroundColor = 'rgb(248, 240, 227)'),
    children = dbc.Row(

        justify = 'center',
        children = [

            # project <
            # feed <
            projectFunction(),
            feedFunction()

            # >

        ]

    )

)


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
