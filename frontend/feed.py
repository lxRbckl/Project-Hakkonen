# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from lxRbckl import githubGet, jsonLoad, githubCreate, githubSet

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
                    # warning <
                    html.Hr(),
                    html.Div(children = contentFunction(pData = gData)),
                    dbc.Alert(

                        is_open = False,
                        color = 'danger',
                        dismissable = True,
                        id = 'warningAlertId',
                        children = 'There was an error updating the feed.json file.'

                    ),

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

    Output('warningAlertId', 'is_open'),

    Input('updateButtonId', 'n_clicks'),
    Input('contentDelButtonId', 'n_clicks'),
    Input('subjectDelButtonId', 'n_clicks'),

    State('contentLoadId', 'value'),
    State('subjectLoadId', 'value'),
    State('contentCreateId', 'value'),
    State('subjectCreateId', 'value'),

    State('linkInputId', 'value'),
    State('imageInputId', 'value'),
    State('borderInputId', 'value'),
    State('contentInputId', 'value'),
    State('textColorInputId', 'value'),
    State('titleColorInputId', 'value'),
    State('backgroundInputId', 'value'),


)
def updateCallback(

        pClick: int,
        pContentDel: int,
        pSubjectDel: int,

        pContentLoad: str,
        pSubjectLoad: str,
        pContentCreate: str,
        pSubjectCreate: str,

        pLinkInput: str,
        pImageInput: str,
        pBorderInput: str,
        pContentInput: str,
        pTextColorInput: str,
        pTitleColorInput: str,
        pBackgroundInput: str

):
    ''' '''

    # try if (success) <
    # except then (failure) <
    try:

        # if (del content) <
        # if (del subject) <
        # elif (add) <
        if (pContentDel): del gData['content'][pContentLoad]
        if (pSubjectDel): del gData['content'][pSubjectLoad]['subject'][pSubjectLoad]
        elif (pClick):

            data = insertFunction(

                pContentLoad = pContentLoad,
                pSubjectLoad = pSubjectLoad,
                pContentCreate = pContentCreate,
                pSubjectCreate = pSubjectCreate,

                pLinkInput = pLinkInput,
                pImageInput = pImageInput,
                pBorderInput = pBorderInput,
                pContentInput = pContentInput,
                pTextColorInput = pTextColorInput,
                pTitleColorInput = pTitleColorInput,
                pBackgroundInput = pBackgroundInput

            )

        # >

        # update <


        # >

        return False

    except: return True

    # >

    # # if (del content) <
    # # if (del subject) <
    # # elif (add) <
    # if (pContentDel): del gData['content'][pContentLoad]
    # if (pSubjectDel): del gData['content'][pSubjectLoad]['subject'][pSubjectLoad]
    # elif (pClick):
    #
    #     try:
    #
    #         # subject = [pSubjectCreate, pTextColorInput, pContentInput]
    #         feed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')
    #         content = jsonLoad(pFile = f'{gDirectory}/backend/template/content.json')
    #
    #         rData = feed
    #         rData['feed']['link'] = pLinkInput
    #         rData['feed']['image'] = pImageInput
    #         rData['feed']['border'] = pBorderInput
    #
    #         # if (create content fresh) <
    #         # if (create subject fresh) <
    #         # if (create content existing) <
    #         # if (create subject existing) <
    #         if (pContentCreate and (not pContentLoad)): sort = [pContentCreate]
    #         if (pSubjectCreate and (not pSubjectLoad)): sort =
    #
    #         # >
    #
    #         # # if (create independent content) <
    #         # # if (create independent subject) <
    #         # # if (create dependent content) <
    #         # # if (create dependent subject) <
    #         #
    #         #
    #         # if (pContentCreate and pContentLoad):
    #         #
    #         #     index = list(gData['content'].keys()).index(pContentLoad)
    #         #     for c, k in enumerate(gData['content'].keys()):
    #         #
    #         #         if (index == c):
    #         #
    #         #             rData['feed']['content'] =
    #         #
    #         #         else: pass
    #         #
    #         # if (pSubjectCreate and pSubjectLoad):
    #         #
    #         #     index = pSubjectLoad
    #         #
    #         # # >
    #
    #         return False
    #
    #     except: return True
    #
    # # >
    #
    # # # if (del) <
    # # # elif (add) <
    # # if (pContentDel): del gData['content'][pContentLoad]
    # # elif (pSubjectDel): del gData['content'][pSubjectLoad]['subject'][pSubjectLoad]
    # # elif (pClick):
    # #
    # #     # if (create content) <
    # #     # if (create subject) <
    # #     if (pContentCreate): index = list(gData['content'].keys()).index(pContentLoad)
    # #     if (pSubjectCreate): index = pSubjectLoad
    # #
    # #     # >
    # #
    # #     subject = [pSubjectCreate, pTextColor, pContent]
    # #
    # #
    # # # >
    # #
    # # return None
