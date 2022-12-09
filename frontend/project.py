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

        width = 5,
        id = 'projectColId'

    )


@application.callback(

    Output('projectColId', 'children'),

    Input('projectColId', 'children')

)
def colCallback(pChildren: list):
    '''  '''

    # local <
    token: dict = jsonLoad(pFile = 'backend/data/token.json')

    # >

    return [

        # header <
        # refresh <
        dbc.Row(

            justify = 'between',
            children = [

                # title <
                # refresh <
                dbc.Col(

                    width = 'auto',
                    children = html.H1(children = 'Project Hakkonen')

                ),
                dbc.Col(

                    width = 'auto',
                    align = 'center',
                    children = dbc.Button(

                        size = 'sm',
                        children = '↻',
                        id = 'refreshButtonId'

                    )

                )

                # >

            ]

        ),
        html.Hr(style = dict(marginTop = '-1%')),

        # >

        # iterate (user) <
        *[html.Div(

            children = [

                # token <
                # project <
                dbc.InputGroup(

                    size = 'sm',
                    children = [

                        dbc.InputGroupText(u),
                        dbc.Input(

                            value = token[u],
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

                ),
                html.Hr()

                # >

            ]

        ) for u in gUser],

        # >

        # submit <
        dbc.Button(

            children = 'Submit',
            id = 'submitButtonId',

        )

        # >

    ]


@application.callback(

    [Output(f'{u}InputId', 'value') for u in gUser],

    Input('submitButtonId', 'n_clicks'),

    [State(f'{u}InputId', 'value') for u in gUser]

)
def submitCallback(

        pClick: int,
        *args

):
    '''  '''

    # set (token) <
    # update token <
    token = jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')
    for t, u in zip(args, gUser): token[u] = t

    # >

    # if (click) then update <
    if (pClick): jsonDump(

        pData = token,
        pFile = f'{gDirectory}/backend/data/token.json'

    )

    # >

    try: return [token[u] for u in gUser]
    except: return [None for u in gUser]
