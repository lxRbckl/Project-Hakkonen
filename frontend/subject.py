# import <
from dash import html
import dash_bootstrap_components as dbc

# >


def subjectFunction(

        pData: dict,
        pSubjectLoad: list,
        pContentLoad: str,
        pContentCreate: str

):
    '''  '''

    # local <
    pType, pColor, pContent = pSubjectLoad
    try: background = pData['content'][pContentLoad]['background']
    except: background = None

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

                    # del <
                    # title <
                    # background <
                    # title color <
                    dbc.Button(

                        children = '🗑',
                        color = 'danger',
                        id = 'contentDelButtonId'

                    ),
                    dbc.InputGroupText(children = pContentLoad if (pContentLoad) else pContentCreate),
                    dbc.Input(

                        id = 'backgroundInputId',
                        placeholder = 'Background',
                        value = None if (background == True) else background

                    ),
                    dbc.Input(

                        id = 'titleColorInputId',
                        placeholder = 'Title Color',
                        value = pData['content'][pContentLoad]['title'] if (pContentLoad) else None

                    )

                    # >

                ]

            ),

            # >

            # del <
            # subject <
            # text color <
            dbc.InputGroup(

                size = 'sm',
                style = dict(marginBottom = '0.5%'),
                children = [

                    # type <
                    # color <
                    # content <
                    dbc.Button(

                        children = '🗑',
                        color = 'danger',
                        id = 'subjectDelButtonId'

                    ),
                    dbc.InputGroupText(children = pType.title()),
                    dbc.Input(

                        id = 'textColorInputId',
                        value = pColor if (pColor) else None,
                        disabled = {

                            'space' : True,
                            'image' : True,
                            'text' : False,
                            'markdown' : True,
                            'subtitle' : False

                        }[pType],
                        placeholder = {

                            'space' : '',
                            'image' : '',
                            'markdown' : '',
                            'text' : 'Text Color',
                            'subtitle' : 'Text Color'

                        }[pType]

                    ),
                    dbc.Input(

                        id = 'contentInputId',
                        value = pContent if (pContent) else None,
                        disabled = True if (pType in ['space']) else False,
                        placeholder = {

                            'space' : '',
                            'image' : 'Image Link',
                            'markdown' : 'Markdown Link',
                            'subtitle' : 'Subtitle Text'

                        }[pType]

                    ) if (pType not in ['text']) else None,

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
