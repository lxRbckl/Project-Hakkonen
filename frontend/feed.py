# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from lxRbckl import githubGet, jsonLoad, githubCreate, githubSet

from frontend.content import contentFunction
from backend.resource import application, gGithub, gUser, gDirectory

# >


# global <
gData = jsonLoad(pFile = 'backend/template/feed.json')['feed']

# >


def feedFunction():
    '''  '''

    return dbc.Col(

        width = 6,
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

    try:

        if (args.count(None) == len(gUser)): gData = None
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

                    # message <
                    dbc.FormText(children = 'Parameters representative of the entire project.'),

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
                        className = 'float-end',
                        style = dict(marginBottom = '1%')

                    )

                    # >

                ]

    except:

        repository = args[1] if (args[1]) else args[0]
        token = jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')
        feed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')

        # try if (feed.json exists) <
        # except then (no feed.json) <
        # finally (notify user ) <
        try: gGithub.get_repo(repository).get_contents(path = 'feed.json')
        except:

            githubCreate(

                pData = feed,
                pBranch = 'main',
                pFile = 'feed.json',
                pRepository = repository,
                pMessage = 'Added feed.json by Project Hakkonen',
                pGithub = Github(token[repository.split('/')[0]])

            )

        finally: return dbc.Alert(

            is_open = True,
            color = 'danger',
            dismissable = True,
            style = dict(marginTop = '1%'),
            children = 'feed.json file added. Please clear and refresh.'

        )

        # >


@application.callback(

    Output('updateButtonId', 'n_clicks'),

    Input('updateButtonId', 'n_clicks'),
    Input('deleteButtonId', 'n_clicks'),

    State('contentCreateId', 'value'),
    State('contentLoadId', 'value'),
    State('subjectCreateId', 'value'),
    State('subjectLoadId', 'value'),

    State('backgroundInputId', 'value'),
    State('titleColorInputId', 'value'),
    State('textColorInputId', 'value'),
    State('contentInputId', 'value')

)
def updateCallback(

        pClick: int,
        pDeleteClick: int,

        pContentCreate: str,
        pContentLoad: str,
        pSubjectCreate: str,
        pSubjectLoad: str,

        pBackgroundInput: str,
        pTitleColor: str,
        pTextColor: str,
        pContent: str

):
    ''' '''

    print(gData) # remove

    # if there is create, then load needs to exist
    # we will insert create AFTER load
    # if there are no loads- then insert it plainly

    print()
    print('content create: ', pContentCreate)
    print('content load: ', pContentLoad)
    print('subject create: ', pSubjectCreate)
    print('subject load: ', pSubjectLoad)

    print('delete: ', pDeleteSwitch)
    print('background: ', pBackgroundInput)
    print('title color: ', pTitleColor)
    print('text color: ', pTextColor)
    print('content: ', pContent)
    print()



    return None
