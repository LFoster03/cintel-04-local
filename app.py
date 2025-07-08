import palmerpenguins
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from shiny import reactive, render, req
from shiny.express import input, ui
from shinywidgets import render_plotly

# Load penguins dataset
penguins_df = palmerpenguins.load_penguins().dropna()

# ----- Page Setup -----
ui.page_opts(title="Penguin Data Exploration Histograms", fillable=True)

# ----- Sidebar -----
with ui.sidebar(open="open"):
    ui.h2("Sidebar")

    ui.input_selectize(
        "selected_attribute",
        "Select Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    )

    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 20)

    ui.input_slider("seaborn_bin_count", "Seaborn Bin Count", 5, 50, 20)

    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
        inline=True
    )

    # Add island checkbox group
    ui.input_checkbox_group(
        "selected_island_list",
        "Select Islands",
        ["Biscoe", "Dream", "Torgersen"],
        selected=["Biscoe", "Dream", "Torgersen"],
        inline=True
    )

    ui.hr()

    ui.a("GitHub", href="https://github.com/LFoster03/cintel-03-reactive/tree/main", target="_blank")


# ----- Reactive Filter -----
@reactive.calc
def filtered_penguins():
    req(input.selected_species_list())
    req(input.selected_island_list())
    species_selected = input.selected_species_list()
    island_selected = input.selected_island_list()
    species_match = penguins_df["species"].isin(species_selected)
    island_match = penguins_df["island"].isin(island_selected)
    return penguins_df[species_match & island_match]


# ----- Data Table + Data Grid -----
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Data Table: Filtered Species & Islands")

        @render.data_frame
        def table_view():
            return render.DataTable(filtered_penguins())

    with ui.card(full_screen=True):
        ui.card_header("Data Grid: Filtered Species & Islands")

        @render.data_frame
        def grid_view():
            return render.DataGrid(filtered_penguins())


# ----- Plotly & Seaborn Histograms -----
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Histogram: Species")

        @render_plotly
        def plotly_histogram():
            df = filtered_penguins()
            attr = input.selected_attribute()
            bins = input.plotly_bin_count()
            if attr and bins:
                return px.histogram(df, x=attr, nbins=bins, color="species", title=f"Plotly Histogram of {attr}")

    with ui.card(full_screen=True):
        ui.card_header("Seaborn Histogram: Species")

        @render.plot
        def seaborn_histogram():
            df = filtered_penguins()
            attr = input.selected_attribute()
            bins = input.seaborn_bin_count()
            if attr and bins:
                plt.figure(figsize=(6, 4))
                sns.histplot(data=df, x=attr, hue="species", bins=bins)
                plt.title(f"Seaborn Histogram of {attr}")
                plt.tight_layout()


# ----- Plotly Scatterplot -----
with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        df = filtered_penguins()
        return px.scatter(
            df,
            x="bill_length_mm",
            y="flipper_length_mm",
            color="species",
            symbol="species",
            size="body_mass_g",
            hover_data=["species", "island"],
            title="Scatterplot of Bill Length vs Flipper Length"
        )

# ----- Island Histogram -----
with ui.card(full_screen=True):
    ui.card_header("Penguin Count by Species and Island")

    @render_plotly
    def species_island_histogram():
        df = filtered_penguins()
        if not df.empty:
            return px.histogram(
                df,
                x="species",              # You can also try "island" here
                color="island",           # Try color="species" if you flip axes
                barmode="group",
                title="Count of Penguins by Species and Island"
            )
        else:
            # Show empty chart message
            return px.histogram(
                pd.DataFrame({"x": [], "y": []}),
                title="No data to display. Try adjusting filters."
            )
