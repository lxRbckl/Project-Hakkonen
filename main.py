# Project Hakkonen by Alex Arbuckle #


# import <
import dash_bootstrap_components as dbc

from backend.resource import application
from frontend.col.feed import feedFunction
from frontend.col.project import projectFunction

# >


application.layout = dbc.Container(

    fluid = True,
    style = dict(backgroundColor = 'rgb(248, 240, 227)'),
    children = dbc.Row(

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
