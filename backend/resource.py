# import <
from os import path
from dash import Dash
from github import Github
from lxRbckl import requestsGet
from dash_bootstrap_components import themes

# >


# global <
githubToken = ''
gUserLink = 'https://github.com/lxRbckl/Project-Skotak/raw/main/setting.json'

gGithub = Github(githubToken)
gUser = requestsGet(pLink = gUserLink)['user']['add']
gDirectory = '/'.join(path.realpath(__file__).split('/')[:-2])
application = Dash(

    name = 'Hakkonen',
    title = 'Hakkonen',
    suppress_callback_exceptions = True,
    external_stylesheets = [

        themes.GRID,
        themes.BOOTSTRAP

    ]

)

# >
