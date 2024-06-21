import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
def top_3_movies_2016(df):
    movies_2016 = df[df['Year'] == 2016]
    top_3_movies = movies_2016.nlargest(3, 'Rating')[['Title', 'Rating']]
    print("Top-3 movies with the highest ratings in 2016:")
    for i, row in top_3_movies.iterrows():
        print(f"Top {i+1}: {row['Title']} with rating {row['Rating']}")

a = top_3_movies_2016(df)

def most_prolific_director(df):
    director_counts = df['Director'].value_counts()
    most_director = director_counts.idxmax()
    count = director_counts.max()
    print(f"The director who involves in the most movies is {most_director} with {count} movies.")

b = most_prolific_director(df)

def highest_revenue_actor(df):
    actor_revenues = {}
    for index, row in df.iterrows():
        actors = row['Actors'].split('|')
        revenue = row['Revenue (Millions)']
        if not pd.isna(revenue):
            for actor in actors:
                if actor in actor_revenues:
                    actor_revenues[actor] += revenue
                else:
                    actor_revenues[actor] = revenue
    highest_actor = max(actor_revenues, key=actor_revenues.get)
    print(f"The actor generating the highest total revenue is {highest_actor} with total revenue of ${actor_revenues[highest_actor]:.2f} million.")

c = highest_revenue_actor(df)

def average_rating_emma_watson(df):
    emma_watson_movies = df[df['Actors'].str.contains('Emma Watson')]
    average_rating = emma_watson_movies['Rating'].mean()
    print(f"The average rating of Emma Watson’s movies is {average_rating:.2f}.")

d = average_rating_emma_watson(df)

def top_4_actors_most_movies(df):
    actor_counts = {}
    for actors in df['Actors']:
        for actor in actors.split('|'):
            if actor in actor_counts:
                actor_counts[actor] += 1
            else:
                actor_counts[actor] = 1
    top_4_actors = sorted(actor_counts.items(), key=lambda x: x[1], reverse=True)[:4]
    print("Top-4 actors playing the most movies:")
    for i, (actor, count) in enumerate(top_4_actors, start=1):
        print(f"Top {i}: {actor} with {count} movies")

e = top_4_actors_most_movies(df)

def top_7_director_actor_pairs(df):
    collaboration_counts = {}
    for index, row in df.iterrows():
        director = row['Director']
        actors = row['Actors'].split('|')
        for actor in actors:
            if (director, actor) in collaboration_counts:
                collaboration_counts[(director, actor)] += 1
            else:
                collaboration_counts[(director, actor)] = 1
    top_7_pairs = sorted(collaboration_counts.items(), key=lambda x: x[1], reverse=True)[:7]
    print("Top-7 frequent collaboration pairs of director & actor:")
    for i, ((director, actor), count) in enumerate(top_7_pairs, start=1):
        print(f"Top {i}: {director} & {actor} with {count} collaborations")

f = top_7_director_actor_pairs(df)

def top_3_directors_most_actors(df):
    director_actors = {}
    for index, row in df.iterrows():
        director = row['Director']
        actors = row['Actors'].split('|')
        if director not in director_actors:
            director_actors[director] = set()
        for actor in actors:
            director_actors[director].add(actor)
    top_3_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    print("Top-3 directors who collaborate with the most actors:")
    for i, (director, actors) in enumerate(top_3_directors, start=1):
        print(f"Top {i}: {director} with {len(actors)} actors")

g = top_3_directors_most_actors(df)

def top_6_actors_most_genres(df):
    actor_genres = {}
    for index, row in df.iterrows():
        genres = row['Genre'].split('|')
        actors = row['Actors'].split('|')
        for actor in actors:
            if actor not in actor_genres:
                actor_genres[actor] = set()
            for genre in genres:
                actor_genres[actor].add(genre)
    top_6_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)[:6]
    print("Top-6 actors playing in the most genres of movies:")
    for i, (actor, genres) in enumerate(top_6_actors, start=1):
        print(f"Top {i}: {actor} with {len(genres)} genres")

h = top_6_actors_most_genres(df)

def top_3_actors_max_gap(df):
    actor_years = {}
    for index, row in df.iterrows():
        year = row['Year']
        actors = row['Actors'].split('|')
        for actor in actors:
            if actor not in actor_years:
                actor_years[actor] = []
            actor_years[actor].append(year)
    actor_gaps = {actor: max(years) - min(years) for actor, years in actor_years.items()}
    top_3_actors = sorted(actor_gaps.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top-3 actors whose movies lead to the largest maximum gap of years:")
    for i, (actor, gap) in enumerate(top_3_actors, start=1):
        print(f"Top {i}: {actor} with a gap of {gap} years")

i = top_3_actors_max_gap(df)