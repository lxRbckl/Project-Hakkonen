# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from lxRbckl import githubSet, githubGet, jsonLoad

from content.text import textFunction
from content.image import imageFunction
from content.space import spaceFunction
from content.subtitle import subtitleFunction
from content.markdown import markdownFunction
from resource import application, gGithub, lxRbckl, ala2q6, gUser

# >


# global <
gData = jsonLoad(pFile = 'template/feed.json')['feed']

# >


def feedFunction():
    '''  '''

    return dbc.Col(

        width = 8,
        id = 'feedColId'

    )


@application.callback(

    Output('feedColId', 'children'),
    [Input(f'{i}DropdownId', 'value') for i in gUser]

)
def projectCallback(*args):
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

                # title <
                html.H2(c.split('/')[1].replace('-', ' ')),
                html.Hr(),

                # >

                # link <
                # border <
                # background <
                dbc.Label('Link'),
                dbc.Input(id = 'linkId', value = gData['link']),
                dbc.FormText('Does this project have a website?'),
                html.Div(style = dict(paddingBottom = '1%')),

                dbc.Label('Border'),
                dbc.Input(id = 'borderId', value = gData['border']),
                dbc.FormText('Does this project have a border color?'),
                html.Div(style = dict(paddingBottom = '1%')),

                dbc.Label('Image'),
                dbc.Input(id = 'imageId', value = gData['image']),
                dbc.FormText('Does this project have an image?'),

                # >

                # content <
                html.Hr(),
                dcc.Dropdown(

                    id = 'contentDropdownId',
                    placeholder = 'Select Content...',
                    options = [

                        {

                            'label' : t,
                            'value' : t

                        }

                    for t in gData['content']]

                ),
                html.Div(id = 'contentDivId'),
                html.Div(id = 'subjectDivId'),

                # >

                # submit <
                html.Hr(),
                dbc.Button(id = 'feedSubmitId', children = 'Submit')

                # >

            ]


@application.callback(

    Output('contentDivId', 'children'),
    Input('contentDropdownId', 'value')

)
def contentCallback(pContent: str):
    '''  '''

    try:

        return dcc.Dropdown(

            id = 'subjectDropdownId',
            placeholder = 'Select Subject...',
            style = dict(

                marginTop = '1%',
                marginBottom = '1%'

            ),
            options = [

                {

                    'label' : f'{c}. {t}',
                    'value' : c

                }

            for c, (t, i, j) in enumerate(gData['content'][pContent]['subject'])]

        )

    except: return None


@application.callback(

    Output('subjectDivId', 'children'),
    Input('subjectDropdownId', 'value'),
    State('contentDropdownId', 'value')

)
def subjectCallback(

        pSubject: int,
        pContent: str

):
    '''  '''

    print(gData) # remove
    print(gData['content'][pContent]['subject'][0]) # remove

    if (not pSubject or not pContent): return None
    else:

        return dbc.Card(

            style = dict(padding = '1%'),
            children = {

                'text' : textFunction,
                'image' : imageFunction,
                'space' : spaceFunction,
                'markdown' : markdownFunction,
                'subtitle' : subtitleFunction

            }[gData['content'][pContent]['subject'][0][0]]

        )
