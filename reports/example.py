import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'
    df = pl.read_csv(url, infer_schema_length=2000000)
    df

    return (df,)


@app.cell
def _(mo):
    name = mo.ui.text()
    return


@app.cell
def _(df, pl):
    filtered = df.filter(pl.col('name') == 'Chris')
    filtered
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

    #testing this
