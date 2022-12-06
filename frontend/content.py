# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import application
from frontend.subject import subjectFunction

# >


# global <
gData = None

# >


def contentFunction(pData: dict):
    '''  '''

    global gData
    gData = pData

    return [

        # content <
        # subject <
        dbc.InputGroup(

            size = 'sm',
            style = dict(marginBottom = '0.5%'),
            children = [

                dbc.InputGroupText(children = 'Content'),
                dbc.Input(id = 'contentCreateId', placeholder = 'Create content...'),
                dbc.Select(

                    id = 'contentLoadId',
                    placeholder = 'Load content...',
                    options = [{'label' : i, 'value' : i} for i in pData['content'].keys()]

                )

            ]

        ),
        dbc.InputGroup(

            size = 'sm',
            style = dict(marginBottom = '0.5%'),
            children = [

                dbc.InputGroupText(children = 'Subject'),
                dbc.Select(

                    id = 'subjectCreateId',
                    placeholder = 'Create subject...',
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

        html.Div(id = 'subjectDivId')

    ]


@application.callback(

    Output('subjectLoadId', 'options'),
    Input('contentLoadId', 'value')

)
def contentCallback(pContent: str):
    '''  '''

    if (not pContent): return None
    else:

        return [

            {

                'value' : c,
                'label' : f'{c}. {i[0]}'

            }

        for c, i in enumerate(gData['content'][pContent]['subject'])]


@application.callback(

    Output('subjectDivId', 'children'),
    Input('subjectLoadId', 'value'),
    Input('subjectCreateId', 'value'),
    State('contentLoadId', 'value')

)
def subjectCallback(

        pSubjectLoad: int,
        pSubjectCreate: str,
        pContentLoad: str,

        pType: str = None,
        pColor: str = None,
        pContent: str = None

):
    '''  '''

    # try if (existing) <
    # except then (new) <
    # finally (return subject) <
    try: subject = gData['content'][pContentLoad]['subject'][int(pSubjectLoad)]
    except: subject = [pSubjectCreate, None, None]
    finally: return subjectFunction(pSubject = subject)

    # >
