The most current version of this workshop including updated and additional material is [here](https://github.com/bettercodepaul/data-wrangling-workshop).

(deutsche Version: [🇩🇪](#deutsche-Version))
# data2day 2023 - Hands-on workshop Polars: The Turbo Boost for Dataframes

Material (notebooks and data) for the hands-on workshop "Polars: The Turbo Boost for Dataframes" at data2day 2023 by [BettercallPaul](https://www.bcxp.de).

The data on which the workshop is based are daily charts from Spotify from 2017-2021 for different countries.

The ingredients that make the workshop interesting and entertaining:

- 👐 Strict focus on practical application from the very beginning
- 💪 25 exercises of increasing difficulty to make sure you can apply the concepts in practice
- 😀 an exercise system that includes on-demand hints and solutions make exercises fun
- 😮 surprising insights: What are the most popular Christmas songs? Which songs are suitable for a romantic evening?
- 🎧 the possibility to listen to your data wrangling: every song can be played directly in the jupyter notebook

For an introduction to Polars we recommend watching this talk from PyCon/PyData Berlin 2023 first: https://www.youtube.com/watch?v=CtkMzCIXOWk

## Prerequisites

You should have basic knowledge of a structured data processing technology, e.g. Pandas, SQL or Apache Spark.

## Using the notebooks

### Colab

The easiest way is to open the notebooks in Google Colab:

- [Colab Intro](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/colab_intro_en.ipynb) - Optional, if you don't know Jupyter/Colab
- [Part 1](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Part_1.ipynb) - load, select, filter & sort
- [Part 2](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Part_2.ipynb) - aggregations, joins & reshaping
- [Part 3](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Part_3.ipynb) - custom expressions, lazy mode and streaming

### Local environment

A local environment is also possible. You may have to make a few adjustments to the notebooks and install Graphviz to display the execution plans.

- `python -m venv venv` or `python3 -m venv venv` or on Windows `py -3.10 -m venv venv`
- `pip install --ignore-installed -r requirements.txt`

## Additional material

- technical backgrounds from Ritchie, the original developer of Polars: http://www.ritchievink.com/blog/2021/02/28/i-wrote-one-of-the-fastest-dataframe-libraries/
- the cheat sheet: https://franzdiebold.github.io/polars-cheat-sheet/Polars_cheat_sheet.pdf

## Feedback

If you like the material please leave us a star.

Bugs, suggestions or request for additional topics? [Create an issue](https://github.com/bettercodepaul/data2day_2023_polars/issues/new/choose)!

Would you like support for your data analytics/machine learning project? We'd love to help, you just [BettercallPaul](mailto:sayhi@bcxp.de).

---

#### deutsche Version
# data2day 2023 - Praxisworkshop Polars: Der Turbo Boost für Dataframes

Material (Notebooks und Daten) für den Praxisworkshop "Polars: Der Turbo-Boost für Dataframes" auf der data2day 2023 von [BettercallPaul](https://www.bcxp.de).

Die Daten, auf denen der Workshop basiert, sind tägliche Charts von Spotify von 2017-2021 für verschiedene Länder.

Die Zutaten, die den Workshop interessant und unterhaltsam machen:

- 👐 Strikter Fokus auf die praktische Anwendung von Anfang an
- 💪 25 Übungen mit steigendem Schwierigkeitsgrad, um sicherzustellen, dass du die Konzepte in der Praxis anwenden kannst
- 😀 ein Übungssystem mit On-Demand-Tipps und Lösungen sorgt dafür, dass die Übungen Spaß machen
- 😮 überraschende Insights: Welches sind die beliebtesten Weihnachtslieder? Welche Lieder eignen sich für einen romantischen Abend?
- 🎧 die Möglichkeit, sich die eigenen Datenanalysen anzuhören: Jedes Lied kann direkt im Jupyter-Notebook abgespielt werden

Für eine Einführung in Polars empfehlen wir, zunächst diesen Vortrag von der PyCon/PyData Berlin 2023 anzusehen: https://www.youtube.com/watch?v=CtkMzCIXOWk

## Voraussetzungen

Du solltest Grundkenntnisse in einer strukturierten Datenverarbeitungstechnologie haben, z.B. Pandas, SQL oder Apache Spark.

## Nutzung der Notebooks

### Colab

Am einfachsten ist es die Notebooks in Google Colab zu öffnen:

- [Colab Intro](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/colab_intro.ipynb) - Optional, falls Jupyter/Colab nicht bekannt ist
- [Teil 1](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Teil_1.ipynb) - Laden, Select, Filtern & Sortieren
- [Teil 2](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Teil_2.ipynb) - Aggregationen, Joins & Reshaping
- [Teil 3](https://colab.research.google.com/github/bettercodepaul/data2day_2023_polars/blob/main/data2day_2023_Polars_Teil_3.ipynb) - Custom Expressions, Lazy Mode und Streaming

### Lokale Umgebung

Eine lokale Umgebung ist auch möglich. Gegebenenfalls müsst ihr ein paar Anpassungen an den Notebooks vornehmen und für die Anzeige der Ausführungspläne Graphviz installieren.

- `python -m venv venv` or `python3 -m venv venv` oder in Windows `py -3.10 -m venv venv`
- `pip install --ignore-installed -r requirements.txt`

## Zusätzliches Material

- technische Hintergründe von Ritchie, dem ursprünglichen Entwickler von Polars: http://www.ritchievink.com/blog/2021/02/28/i-wrote-one-of-the-fastest-dataframe-libraries/

- ein Cheat-Sheet: https://franzdiebold.github.io/polars-cheat-sheet/Polars_cheat_sheet.pdf

## Feedback

Wenn dir das Material gefällt, hinterlasse uns bitte einen Stern.

Bugs, Vorschläge oder Wünsche für zusätzliche Themen? [Erstelle ein Ticket](https://github.com/bettercodepaul/data2day_2023_polars/issues/new/choose)!

Benötigst du Unterstützung für dein Projekt im Bereich Data Analytics/Machine Learning? Wir würden uns freuen zu helfen, you just [BettercallPaul](mailto:sayhi@bcxp.de).
