""" Activity Dash learning
    Created on 04-12-2020, 10:23
    @author Alejo Cain """

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
#all the html
app.layout = html.Div(children=[
    html.H1('Bijna tijd voor bier ')],
    ) # is going to contain ID styles so label all the things!

if __name__ == '__main__':
    app.run_server(debug=True)


