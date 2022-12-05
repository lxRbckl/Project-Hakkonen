# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import application

# >


# global <
gData = None

# >


def contentFunction(

        # pType: str = None,
        # pColor: str = None,
        # pContent: str = None

        pData: dict

):
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

                    id = 'subjectSelectId',
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

        for c, i in enumerate(gData['content'][pContent]['subject'], start = 1)]


@application.callback(

    Output('subjectDivId', 'children'),
    Input('subjectLoadId', 'value'),
    State('contentLoadId', 'value')

)
def subjectCallback(

        pSubject: int,
        pContent: str

):
    '''  '''

    # gData['content'][pContent]['subject'][int(pSubject)]
    # output: [pType, pColor, pContent]

    return None
