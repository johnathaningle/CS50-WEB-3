from booknetwork import db
from booknetwork.models import Book
import pandas as pd

dataset = pd.read_csv('books.csv', sep=',')

for i in dataset.values:
    isbn = str(i[0])
    title = str(i[1])
    author = str(i[2])
    year_published = int(i[3])
    bk = Book(isbn=isbn, title=title, author=author, year_published=year_published)
    db.session.add(bk)
    db.session.commit()
    print(f'adding {isbn} {title} {author} {year_published}')
