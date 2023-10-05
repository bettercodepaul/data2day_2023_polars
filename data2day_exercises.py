from IPython.display import IFrame
import polars as pl

URL_TRACK_ID_PREFIX = "https://open.spotify.com/track/"

def play_song(df, index=0):
    if "trackId" in df.columns:
        trackId = df.item(index, "trackId")
    elif "url" in df.columns:
        trackId = df.item(index, "url")[len(URL_TRACK_ID_PREFIX):]
    else:
        return("Can not play a song without either column 'url' or 'trackId'")

    url = f"https://open.spotify.com/embed/track/{trackId}?utm_source=generator"
    return(IFrame(src=url, width="100%", height=152, style="border-radius:12px", frameBorder="0", allowfullscreen="", allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture", loading="lazy"))


def assert_approx(actual, expected, tol=0.001):
    assert abs(actual - expected) < abs(tol*expected)


class HintSolution:

    def __init__(self, question, check, hint, solution):
        self.tries = 1
        self._question = question
        self._hint = hint
        self._check = check
        self._solution = solution

    def question(self):
        print(self._question)

    def hint(self):
        print(self._hint)

    def solution(self):
        print(self._solution)

    def check(self, *args):
        try:
            self._check(*args)
            check_result = True
        except:
            check_result = False
        
        if check_result:
            if self.tries == 1:
                #print("✅ Wow, first try and you nailed it! You're a natural problem-solver! 🎉👏")
                print("✅ Wow, erster Versuch - du hast es voll drauf! Du bist ein geborener Problemlöser! 🎉👏")
            elif self.tries == 2:
                #print("✅ Right on target! You hit the bullseye on your second shot! 🎯👏")
                print("✅ Voll ins Schwarze getroffen! Schon beim zweiten Schuss mitten auf die Zwölf! 🎯👏")
            elif self.tries == 3:
                #print("✅ Persistence pays off! Third try's a charm, and you did it! 🌟👏")
                print("✅ Durchhalten zahlt sich aus! Mit dem dritten Versuch hast du es geschafft! 🌟👏")
            else:
                #print("✅ It might have taken a few tries, but you're unstoppable! 😅👊")
                print("✅ Es hat vielleicht ein paar Versuche gebraucht, aber du bist nicht aufzuhalten! 😅👊")
                
        else:
            if self.tries == 1:
                #print("🤔 Give it another shot! You're just getting started. 🔍")
                print("🤔 Probier es nochmal! Du hast ja gerade erst angefangen. 🔍")
            elif self.tries == 2:
                #print("🤔 Two tries down, but the solution is within reach. Keep going! 🧐")
                print("🤔 Zwei Versuche hinter dir, aber die Lösung ist in Reichweite. Nur Mut! 🧐")
            elif self.tries == 3:
                #print("🤔 Almost there, just one more push! You can do it! 😬")
                print("🤔 Du bist fast am Ziel, nur noch eine letzte Anstrengung! Du schaffst das! 😬")
            else:
                #print("🤔 It's tough, but don't lose hope! Maybe consider using the hint() method now? 😓")
                print("🤔 Es ist schwierig, aber verlier nicht die Hoffnung! Hast du schon die hint() Methode verwendet? 😓")
            self.tries = self.tries + 1
            

def q1_check(df):
    assert df.shape == (362_182, 4)
    assert df.columns == ["date", "rank", "title", "artist"]

q1 = HintSolution(
    'Selektiere nur die Spalten "date", "rank", "title" und "artist".',
    q1_check,
    'Achte auf die Reihenfolge der Spalten und nutze die Methode "select".',
    'q1_df = df.select(["date", "rank", "title", "artist"])'
)



def q2_check(df):
    assert df.shape == (362_182, 4)
    assert df.columns == ["date", "rank", "title", "performer"]

q2 = HintSolution(
    'Selektiere nur die Spalten "date", "rank", "title" und "artist", aber benenne die Spalte "artist" in "performer" um.',
    q2_check,
    'Du kannst die Funktion "alias" nutzen, um eine Spalte umzubenennen.',
    'q2_df = df.select(["date", "rank", "title", pl.col("artist").alias("performer")])'
)



def q3_check(result):
    if type(result) == pl.dataframe.frame.DataFrame:
        result = result.item(0, 0)
    assert_approx(result, 1_212_938)

q3 = HintSolution(
    'Wie oft wurde ein Lied durchschnittlich pro Tag gestreamt?',
    q3_check,
    'Du kannst pl.col("streams") mit der Funktion "mean" verbinden.',
    'q3_df = df.select(pl.col("streams").mean())'
)



def q4_check(rank_1, rank_200):
    if type(rank_1) == pl.dataframe.frame.DataFrame:
        rank_1 = rank_1.item(0, 0)
    if type(rank_200) == pl.dataframe.frame.DataFrame:
        rank_200 = rank_200.item(0, 0)

    assert_approx(rank_1, 6_452_678)
    assert_approx(rank_200, 604_534)

q4 = HintSolution(
    'Wie oft wurden Lieder auf Platz 1 durchschnittlich pro Tag gestreamt und wie oft die Lieder auf Platz 200?',
    q4_check,
    'So ähnlich wie Frage 3 aber jeweils die Spalte "rank" entsprechend gefiltert.',
    '''
rank_1 = df.filter(pl.col("rank").eq(1)).select(pl.col("streams").mean())
rank_200 = df.filter(pl.col("rank").eq(200)).select(pl.col("streams").mean())
    '''
)


def q5_check(result):
    if type(result) == pl.dataframe.frame.DataFrame:
        result = result.item(0, "title")
    assert result == "DÁKITI"

q5 = HintSolution(
    'Welches Lied war am Sylvesterabend 2017 auf Platz 1? Höre es auch gerne an.',
    q5_check,
    'Filter sowohl auf den 31.12.2017 ("date") als auch auf den Platz 1 ("rank").',
    '''
q5_df = df.filter(pl.col("date").eq(pl.date(2017, 12, 31)) & pl.col("rank").eq(1))
play_song(q5_df)
    '''
)