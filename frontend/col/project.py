# import <
from dash import html, dcc
from lxRbckl import jsonLoad, jsonDump
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import gGithub, gUser, application, gDirectory

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
        token: dict = jsonLoad(pFile = 'backend/data/token.json')

):
    '''  '''

    return [

        # iterate (user) <
        *[html.Div(

            children = [

                html.Hr(),
                dbc.InputGroup(

                    size = 'sm',
                    children = [

                        dbc.InputGroupText(u),
                        dbc.Input(

                            id = f'{u}InputId',
                            placeholder = 'GitHub API Token'

                        )

                    ]

                ),
                dcc.Dropdown(

                    id = f'{u}DropdownId',
                    style = dict(marginTop = '1%'),
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

        # >

        # submit <
        html.Hr(),
        dbc.Button(id = 'projectSubmitId', children = 'Submit')

        # >

    ]


@application.callback(

    [Output(f'{u}InputId', 'value') for u in gUser],
    Input('projectSubmitId', 'n_clicks'),
    [State(f'{u}InputId', 'value') for u in gUser]

)
def submitCallback(

        pClick: int,
        *args

):
    '''  '''

    # local <
    token = jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')


    # >

    # if (click) then update <


    # >

    return [None, None]
