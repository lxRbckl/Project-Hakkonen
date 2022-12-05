# import <
from dash import html
import dash_bootstrap_components as dbc

# >


def subjectFunction(

        pType: str = None,
        pColor: str = None,
        pContent: str = None

):
    '''  '''

    print(pType)
    print(pColor)
    print(pContent)

    return html.H1(id = 'testid', children = 'ok')
