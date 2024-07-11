import json
from models import Author, Quote


def load_authors(file_path: str) -> None:
    # Load authors from a JSON file and save them to the database
    with open(file_path, "r", encoding="utf-8") as file:
        authors_data = json.load(file)
    if isinstance(authors_data, list):
        for item in authors_data:
            if item.get("name"):
                author = Author(
                    fullname=item.get("name"),
                    born_date=item.get("birthdate"),
                    born_location=item.get("born_location"),
                    description=item.get("bio"),
                )
                author.save()
    else:
        if authors_data.get("name"):
            author = Author(
                fullname=authors_data.get("name"),
                born_date=authors_data.get("birthdate"),
                born_location=authors_data.get("born_location"),
                description=authors_data.get("bio"),
            )
            author.save()


def load_quotes(file_path: str) -> None:
    # Load quotes from a JSON file and save them to the database
    with open(file_path, "r", encoding="utf-8") as file:
        quotes_data = json.load(file)
    if isinstance(quotes_data, list):
        for item in quotes_data:
            author_name = item.get("author")
            author = Author.objects(fullname=author_name).first()
            if author:
                quote = Quote(
                    tags=item.get("tags", []),
                    author=author,
                    quote=item.get("text"),
                )
                quote.save()
    else:
        author_name = quotes_data.get("author")
        author = Author.objects(fullname=author_name).first()
        if author:
            quote = Quote(
                tags=quotes_data.get("tags", []),
                author=author,
                quote=quotes_data.get("text"),
            )
            quote.save()


if __name__ == "__main__":
    load_authors("authors.json")
    load_quotes("quotes.json")
