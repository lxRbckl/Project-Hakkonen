# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from lxRbckl import githubSet, githubGet, jsonLoad

from resource import application, gGithub, lxRbckl, ala2q6

# >


def feedFunction():
    '''  '''

    return dbc.Col(

        width = 8,
        id = 'feedColId'

    )


@application.callback(

    Output('feedColId', 'children'),
    Input('ala2q6DropdownId', 'value'),
    Input('lxRbcklDropdownId', 'value')

)
def feedCallback(

        a: str,
        b: str,
        f: dict = jsonLoad(pFile = 'feed.json')['feed']

):
    '''  '''

    if (not a and not b): return None
    else:

        try:

            f = githubGet(

                pGithub = gGithub,
                pFile = 'feed.json',
                pRepository = a if (a) else b

            )['feed']

        except: pass
        finally:

            print(f) # remove
            c = a if (a) else b

            return [

                # title <
                # link <
                # submit <
                html.H2(c.split('/')[1].replace('-', ' ')),

                html.Hr(),
                dbc.Label('Link'),
                dbc.Input(id = 'linkId', value = f['link']),
                dbc.FormText('Does this project have a website?'),

                html.Hr(),
                dbc.Button(id = 'submitId', children = 'Submit')

                # >

            ]
