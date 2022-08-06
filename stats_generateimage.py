import plotly.graph_objects as go
from plotly.subplots import make_subplots
from colorutils import get_random_color_palette
import logging as lg

def generate_stats_image(langstats: dict, activitystats: dict):
    lg.info("Starting to generate random colors!")

    langstatscolorpalette = get_random_color_palette()
    activitystatscolorpalette = langstatscolorpalette

    languages = list(langstats.keys())
    languageSizes = list(langstats.values())

    fig = make_subplots(
        rows=1,
        cols=3,
        column_widths=[0.475, 0.025, 0.5],
        specs=[
            [
                {"type": "pie"},
                None,
                {"type": "bar"}
            ]
        ]
    )

    fig.add_trace(go.Pie(
        labels=languages,
        values=languageSizes,
        hole=.5, 
        textinfo='label+percent', 
        textfont=dict(
            color='white', 
            size=10), 
        marker=dict(
            colors=langstatscolorpalette, 
            line=dict(
                color='rgba(25,25,25,1)', 
                width=5)),
        showlegend=False
    ), row=1, col=1)

    dates = list(activitystats.keys())
    commits = list(activitystats.values())

    fig.add_trace(go.Bar(x=commits,
        y=dates,
        marker_color=activitystatscolorpalette,
        orientation='h',
        ), row=1, col=3
    )

    fig.update_xaxes(zeroline=False,
        tickfont=dict(
            color='white', 
            size=10),
        showgrid=False,
        linecolor='rgba(25,25,25,1)',
        linewidth=2)

    fig.update_yaxes(zeroline=False,
            tickfont=dict(
                color='white', 
                size=10),
            showgrid=False,
            linecolor='rgba(25,25,25,1)',
            linewidth=2)
    fig.update_layout(
        height=400, 
        width=800, 
        margin=go.layout.Margin(
            l=25,
            r=25,
            b=35,
            t=50,
            pad = 4
        ),
        title=dict(
            text='Languages & Activity Log (Commits)', 
            font=dict(
                color='white', 
                size=16), 
            x=.5, 
            y=.95),
        paper_bgcolor='rgba(25,25,25,1)',
        plot_bgcolor='rgba(25,25,25,1)',
        showlegend=False)
    
    fig.write_image("githubstatsimage.png")

    lg.info("Generate Image Completed!")