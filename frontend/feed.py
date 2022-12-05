# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from lxRbckl import githubGet, jsonLoad
from dash.dependencies import Input, Output, State

from frontend.content import contentFunction
from backend.resource import application, gGithub, gUser

# >


# global <
gData = jsonLoad(pFile = 'backend/template/feed.json')['feed']

# >


def feedFunction():
    '''  '''

    return dbc.Col(

        width = 8,
        id = 'feedColId'

    )


@application.callback(

    Output('feedColId', 'children'),
    Input('refreshButtonId', 'n_clicks'),
    [Input(f'{i}DropdownId', 'value') for i in gUser]

)
def colCallback(pClick, *args):
    '''  '''

    global gData

    if (args.count(None) == len(args)): return None
    else:

        try:

            c = [i for i in args if (i)][0]
            gData = githubGet(

                pRepository = c,
                pGithub = gGithub,
                pFile = 'feed.json'

            )['feed']

        except: pass
        finally:

            return [

                # header <
                html.H2(children = c.split('/')[1].replace('-', ' ')),
                html.Hr(style = dict(marginTop = '0.5%')),

                # >

                # link <
                # border <
                # background <
                *[

                    dbc.InputGroup(

                        size = 'sm',
                        style = dict(marginTop = '0.5%'),
                        children = [

                            dbc.InputGroupText(i.title()),
                            dbc.Input(id = f'{i}InputId', value = gData[i])

                        ]

                    )

                for i in ('link', 'border', 'image')],

                # >

                # content <
                html.Hr(),
                html.Div(children = contentFunction(pData = gData)),

                # >

                # update <
                html.Hr(),
                dbc.Button(

                    children = 'Update',
                    id = 'updateButtonId',
                    className = 'float-end'

                )

                # >

            ]
