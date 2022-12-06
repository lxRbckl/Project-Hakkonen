# import <
from dash import html
import dash_bootstrap_components as dbc

# >


def subjectFunction(pSubject: list):
    '''  '''

    # local <
    pType, pColor, pContent = pSubject

    # >

    # if (boot) <
    # else (input) <
    if (not pType): return None
    else:

        return [

            # subject <
            # text <
            html.Hr(),
            dbc.InputGroup(

                size = 'sm',
                style = dict(marginBottom = '0.5%'),
                children = [

                    # type <
                    # color <
                    # content <
                    dbc.InputGroupText(children = pType.title()),
                    dbc.Input(

                        id = 'colorInputId',
                        placeholder = 'Color',
                        value = pColor if (pColor) else None

                    ) if (pType not in ['space']) else None,
                    dbc.Input(

                        id = 'contentInputId',
                        value = pContent if (pContent) else None,
                        placeholder = {

                            'image' : 'Image Link',
                            'markdown' : 'Markdown Link',
                            'subtitle' : 'Subtitle Text'

                        }[pType]

                    ) if (pType not in ['space', 'text']) else None,

                    # >

                ]

            ),
            dbc.Textarea(

                placeholder = 'Text',
                id = 'contentInputId',
                style = dict(height = '15vh'),
                value = pContent if (pContent) else None

            ) if (pType in ['text']) else None

            # >

        ]

    # >
