# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from lxRbckl import jsonLoad, githubGet, githubCreate, githubSet

from backend.insert import  insertFunction
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

                )

            except: pass
            finally:

                return [

                    # header <
                    html.H2(

                        id = 'headerH2Id',
                        children = c.replace('-', ' ')

                    ),
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
                    html.Hr(),

                    # >

                    # warning <
                    # update <
                    dbc.Alert(

                        is_open = False,
                        dismissable = True,
                        id = 'warningAlertId'

                    ),
                    dbc.Button(

                        children = 'Update',
                        id = 'updateButtonId',
                        className = 'float-end',
                        style = dict(marginBottom = '1%')

                    )

                    # >

                ]

    except:

        repository = args[1] or args[0]
        token = jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')
        feed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')

        # try if (feed.json exists) <
        # except then (no feed.json) <
        # finally (notify user of change) <
        try: gGithub.get_repo(repository).get_contents(path = 'feed.json')
        except Exception as e:

            print('e2', e) # remove
            githubCreate(

                pData = feed,
                pBranch = 'main',
                pFile = 'feed.json',
                pRepository = repository,
                pMessage = 'Created by Project Hakkonen',
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

    Output('warningAlertId', 'color'),
    Output('warningAlertId', 'is_open'),
    Output('warningAlertId', 'children'),
    Output('updateButtonId', 'disabled'),

    Input('updateButtonId', 'n_clicks'),
    Input('contentDelButtonId', 'n_clicks'),
    Input('subjectDelButtonId', 'n_clicks'),

    State('headerH2Id', 'children'),

    State('contentLoadId', 'value'),
    State('subjectLoadId', 'value'),
    State('contentCreateId', 'value'),
    State('subjectCreateId', 'value'),

    State('linkInputId', 'value'),
    State('imageInputId', 'value'),
    State('titleInputId', 'value'),
    State('borderInputId', 'value'),
    State('contentInputId', 'value'),
    State('textColorInputId', 'value'),
    State('backgroundInputId', 'value')

)
def updateCallback(

        pClick: int,
        pContentDel: int,
        pSubjectDel: int,

        pHeader: str,

        pContentLoad: str,
        pSubjectLoad: str,
        pContentCreate: str,
        pSubjectCreate: str,

        pLinkInput: str,
        pImageInput: str,
        pTitleInput: str,
        pBorderInput: str,
        pContentInput: str,
        pTextColorInput: str,
        pBackgroundInput: str

):
    ''' '''

    global gData

    # try if (success) <
    # except then (failure) <
    try:

        # if (del content) <
        # elif (del subject) <
        # elif (add) <
        if (pContentDel): del gData['content'][pContentLoad]
        elif (pSubjectDel): del gData['content'][pContentLoad]['subject'][int(pSubjectLoad)]
        elif (pClick):

            gData = insertFunction(

                pData = gData,

                pContentLoad = pContentLoad,
                pSubjectLoad = pSubjectLoad,
                pContentCreate = pContentCreate,
                pSubjectCreate = pSubjectCreate,

                pLinkInput = pLinkInput,
                pImageInput = pImageInput,
                pTitleInput = pTitleInput,
                pBorderInput = pBorderInput,
                pContentInput = pContentInput,
                pTextColorInput = pTextColorInput,
                pBackgroundInput = pBackgroundInput

            )

        # >

        color, children = 'success', 'The feed.json was successfully updated. Please refresh.'

    except: color, children = 'danger', 'There was an error updating the feed.json file.'
    finally:

        githubSet(

            pData = gData,
            pFile = 'feed.json',
            pRepository = pHeader.replace(' ', '-'),
            pMessage = 'Updated by Project Hakkonen',
            pGithub = Github(jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')[pHeader.split('/')[0]])

        )
        return {

            True : (color, True, children, True),
            None: (color, False, children, False),
            False : (color, False, children, False)

        }[(pClick or pContentDel or pSubjectDel)]

    # >
