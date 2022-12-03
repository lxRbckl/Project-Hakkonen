# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from resource import application

# >


def feedFunction(



):
    '''  '''

    return dbc.Col(

        width = 8,
        id = 'feedColId',
        children = [

            html.H2('feed', style = dict(width = 'auto'))

        ]

    )


@application.callback(

    Output('feedColId', 'children'),
    Input('lxRbcklDropdownId', 'value'),
    Input('ala2q6DropdownId', 'value')

)
def few(s, ss):
    '''  '''

    print(s, ss)

    return [html.H1(s), html.H1(ss)]
