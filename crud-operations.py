from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['db_news']
collection = db['articles']




new_article = {
    'title': 'Recent news',
    'paragraph': 'This is a new paragraph',
    'date': '2023-08-14'
}
collection.insert_one(new_article)
print("Article inserted successfully.")


all_articles = collection.find()
for article in all_articles:
    print("Title:", article['title'])
    print("Paragraph:", article['paragraph'])
    print("Date:", article['date'])
    print()


date_query = {'date': '2023-08-14'}
articles_on_date = collection.find(date_query)
for article in articles_on_date:
    print("Title:", article['title'])
    print("Paragraph:", article['paragraph'])
    print("Date:", article['date'])
    print()


filter_query = {'title': 'Dont let the other soldiers watch: Rape as a weapon of war in Sudan'}
update_query = {'$set': {'title': 'Dont let the other soldiers watch: Rape as a weapon of war in India'}}
result = collection.update_one(filter_query, update_query)
if result.modified_count > 0:
    print("Article content updated.")
else:
    print("Article not found.")


delete_query = {'title': 'Five dead as boat carrying refugees sinks off Tunisia'}
result = collection.delete_one(delete_query)
if result.deleted_count > 0:
    print("Article deleted.")
else:
    print("Article not found.")
