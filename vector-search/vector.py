from elasticsearch import Elasticsearch
from openai import OpenAI

es_client = Elasticsearch(
    "https://localhost:9200",
    ssl_assert_fingerprint='<fingerprint>',
    basic_auth=("elastic", "passw0rd")
)
openai_client = OpenAI(api_key='<api_key>')

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "release_year": 2010},
    {"title": "The Shawshank Redemption", "genre": "Drama", "release_year": 1994},
    {"title": "The Godfather", "genre": "Crime", "release_year": 1972},
    {"title": "Pulp Fiction", "genre": "Crime", "release_year": 1994},
    {"title": "Forrest Gump", "genre": "Drama", "release_year": 1994}
]

# Indexing movies
for movie in movies:
    movie['title_embedding'] = openai_client.embeddings.create(
        input=[movie['title']], model='text-embedding-3-small'
    ).data[0].embedding
    es_client.index(index="movies", document=movie)
