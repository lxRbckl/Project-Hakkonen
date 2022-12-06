# import <
from dash import html
import dash_bootstrap_components as dbc

# >


def subjectFunction(

        pData: dict,
        pSubject: list,
        pContentLoad: str

):
    '''  '''

    # print(pContentLoad) # remove
    # print(pData) # remove

    # local <
    pType, pColor, pContent = pSubject

    # >

    # if (boot) <
    # else (input) <
    if (not pType): return None
    else:

        return [

            # content <
            html.Hr(),
            dbc.InputGroup(

                size = 'sm',
                style = dict(marginBottom = '0.5%'),
                children = [

                    # title <
                    # background <
                    # title color <
                    dbc.InputGroupText(children = pContentLoad),
                    dbc.Input(

                        id = 'backgroundInputId',
                        placeholder = 'Background',
                        value = pData['content'][pContentLoad]['background']

                    ),
                    dbc.Input(

                        id = 'titleColorInputId',
                        placeholder = 'Title Color',
                        value = pData['content'][pContentLoad]['title']

                    )

                    # >

                ]

            ),

            # >

            # subject <
            # text color <
            dbc.InputGroup(

                size = 'sm',
                style = dict(marginBottom = '0.5%'),
                children = [

                    # type <
                    # color <
                    # content <
                    dbc.InputGroupText(children = pType.title()),
                    dbc.Input(

                        id = 'textColorInputId',
                        placeholder = 'Text Color',
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

            ) if (pType in ['text']) else None,

            # >

            # message <
            dbc.FormText(children = 'Select Update when finished.')

            # >

        ]

    # >
