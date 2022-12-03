# import <
from dash import html, dcc
from lxRbckl import requestsGet
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from resource import gGithub, gUserLink, application

# >


def projectFunction(



):
    '''  '''

    return dbc.Col(

        width = 4,
        id = 'projectColId'

    )


@application.callback(

    Output('projectColId', 'children'),
    Input('projectColId', 'children')

)
def callbackFunction(p: list):
    '''  '''

    return [

        dcc.Dropdown(

            id = f'{u}DropdownId',
            options = [

                {

                    'label' : r.full_name.split('/')[1],
                    'value' : r.full_name

                }

            for r in gGithub.get_user(u).get_repos()]

        )

    for u in requestsGet(pLink = gUserLink)['user']['add']]
