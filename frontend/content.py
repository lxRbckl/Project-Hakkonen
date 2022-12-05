# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import application

# >


def contentFunction(

        # pType: str = None,
        # pColor: str = None,
        # pContent: str = None

):
    '''  '''

    return [

        # content <
        # subject <
        dbc.InputGroup(

            size = 'sm',
            style = dict(marginBottom = '0.5%'),
            children = [

                dbc.InputGroupText(children = 'Content'),
                dbc.Input(id = 'contentCreateId', placeholder = 'Create content...'),
                dbc.Select(id = f'contentLoadId', placeholder = 'Load content...')

            ]

        ),
        dbc.InputGroup(

            size = 'sm',
            style = dict(marginBottom = '0.5%'),
            children = [

                dbc.InputGroupText(children = 'Subject'),
                dbc.Select(

                    id = 'subjectSelectId',
                    placeholder = 'Select subject...',
                    options = [

                        {'label' : 'text', 'value' : 'text'},
                        {'label' : 'title', 'value' : 'title'},
                        {'label' : 'space', 'value' : 'space'},
                        {'label' : 'image', 'value' : 'image'},
                        {'label' : 'subtitle', 'value' : 'subtitle'},
                        {'label' : 'markdown', 'value' : 'markdown'}

                    ]

                ),
                dbc.Select(

                    id = 'subjectLoadId',
                    placeholder = 'Load subject...'

                )

            ]

        ),

        # >

        html.Div(id = 'contentDivId')

    ]


