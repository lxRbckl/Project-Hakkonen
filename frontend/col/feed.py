# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from lxRbckl import githubGet, jsonLoad
from dash.dependencies import Input, Output, State

from frontend.content.text import textFunction
from frontend.content.image import imageFunction
from frontend.content.space import spaceFunction
from frontend.content.subtitle import subtitleFunction
from frontend.content.markdown import markdownFunction
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
                html.Hr(style = dict(marginTop = '-0.5%')),

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
            style = dict(marginTop = '0.5%'),
            placeholder = 'Select Subject...',
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
