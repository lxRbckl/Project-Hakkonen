# import <
from github import Github
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from lxRbckl import githubGet, jsonLoad, githubCreate

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

        if (args.count(None) == len(gUser)): print('ok'); gData = None
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
                        className = 'float-end'

                    )

                    # >

                ]

    except Exception as e:

        print(e) # remove

        repository = args[1] if (args[1]) else args[0]
        token = jsonLoad(pFile = f'{gDirectory}/backend/data/token.json')
        feed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')

        try: gGithub.get_repo(repository).get_contents(path = 'feed.json')
        except:

            githubCreate(

                pData = feed,
                pBranch = 'main',
                pFile = 'feed.json',
                pRepository = repository,
                pMessage = 'Added feed.json',
                pGithub = Github(token[repository.split('/')[0]])

            )

        finally: return None
