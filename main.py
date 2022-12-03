# Project Hakkonen by Alex Arbuckle #


# import <
import dash_bootstrap_components as dbc

from resource import application
from col.feed import feedFunction
from col.project import projectFunction

# >


application.layout = dbc.Container(

    fluid = True,
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
