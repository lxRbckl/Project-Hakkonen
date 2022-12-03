# import <
from dash import html, dcc
from lxRbckl import jsonLoad, jsonDump
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from resource import gGithub, gUser, application

# >


def projectFunction():
    '''  '''

    return dbc.Col(

        width = 4,
        id = 'projectColId'

    )


@application.callback(

    Output('projectColId', 'children'),
    Input('projectColId', 'children')

)
def colCallback(

        p: list,
        token: dict = jsonLoad(pFile = 'data/token.json')

):
    '''  '''

    return [

        # iterate (user) <
        # submit <
        *[html.Div(

            children = [

                html.Hr(),
                html.H5(u),

                dcc.Dropdown(

                    id = f'{u}DropdownId',
                    placeholder = 'Select Project...',
                    options = [

                        {

                            'label' : r.full_name.split('/')[1].replace('-', ' '),
                            'value' : r.full_name

                        }

                    for r in gGithub.get_user(u).get_repos()]

                )

            ]

        ) for u in gUser],
        html.Hr(),
        dbc.Button(id = 'projectSubmitId', children = 'Submit')

        # >

    ]


@application.callback(

    Output(),
    Input()

)
def buttonCallback():
    '''  '''

    pass
