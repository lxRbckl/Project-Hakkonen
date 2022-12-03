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
        f: dict = jsonLoad(pFile = 'template/feed.json')['feed']

):
    '''  '''

    if (not a and not b): return None
    else:

        try:

            c = a if (a) else b
            f = githubGet(

                pRepository = c,
                pGithub = gGithub,
                pFile = 'feed.json'

            )['feed']

        except: pass
        finally:

            print(f) # remove
            return [

                # title <
                html.H2(c.split('/')[1].replace('-', ' ')),
                html.Hr(),

                # >

                # link <
                # border <
                # background <
                dbc.Label('Link'),
                dbc.Input(id = 'linkId', value = f['link']),
                dbc.FormText('Does this project have a website?'),
                html.Div(style = dict(paddingBottom = '1%')),

                dbc.Label('Border'),
                dbc.Input(id = 'borderId', value = f['border']),
                dbc.FormText('Does this project have a border color?'),
                html.Div(style = dict(paddingBottom = '1%')),

                dbc.Label('Image'),
                dbc.Input(id = 'imageId', value = f['image']),
                dbc.FormText('Does this project have an image?'),

                # >

                # content <
                html.Hr(),

                # >

                # submit <
                html.Hr(),
                dbc.Button(id = 'submitId', children = 'Submit')

                # >

            ]
