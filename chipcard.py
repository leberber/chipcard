
from dash import Dash, dcc, html, Input, Output, _dash_renderer, callback
import plotly.graph_objects as go
import dash_mantine_components as dmc

_dash_renderer._set_react_version("18.2.0")
app = Dash(__name__)


def mantine_card(num):
    return  dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-8.png",
                h=70, 
                alt="Norway",
            )
        ),
        dmc.Group(
            [
                dmc.Text("Norway Fjord Adventures", fw=500),
                dmc.Badge(f" {num}", color="pink", size='xl'),
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and "
            "around the fjords of Norway",
            size="sm",
            c="dimmed",
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    w=300, 
)


def chipcard(children, value, className='chip-card', variant='filled', style ={}):
    defaults = {"padding": "5px 10px", "borderRadius": "12px", "height": "100%", 'color':'black', 'backgroundColor':'transparent','border':'1px solid #f0ebeb'}
    style = {**defaults, **style}
    return dmc.Chip(
            children =children, 
            value=value,
            className = className,
            variant = variant,
            styles = {
                    "label": style,
                    "input": {"display": "none"},  # Prevents resizing
                    "checked": {"transform": "none"},  # Prevent transform effect
                    "iconWrapper": {"display": "none"},  # Hides the checkmark
                }
            )


app.layout = dmc.MantineProvider(
    children=[
        dmc.Box(
             
            children =[
                dmc.ChipGroup(
                    id="chipgroup-single",
                    children =[
                        dmc.Group(
                            children = [
                                chipcard(dmc.Box([mantine_card(i)]), str(i))  for i in range(10)
                            ]
                        )
                    ],
                    multiple=False,
                    value="1",
                ),
                dmc.Center(
                    pt=20,
                    children = [
                        dmc.Text('Clicked Card ', size='30px'), dmc.Text(w=10), dmc.Text(id = 'clicked-card', size='30px')
                    ]
                )
            ]
        )
    ]
)

@callback(
    Output('clicked-card', 'children'),
    Input("chipgroup-single", "value"),
)
def clicked_card_output(value):

    return value
    
if __name__ == "__main__":
    app.run_server(debug=True)