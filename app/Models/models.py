from mongoengine import Document, StringField, connect, disconnect


# Definisanje modela (ekvivalent klase iz EF-a)
class URLs(Document):
    full_url = StringField(required=True, unique=True, max_length=200)
    short_url = StringField(required=True, unique=True, max_length=10)

# Dodavanje jednog zapisa
# url = URLs(full_url="https://example.com", short_url="abc123")
# url.save()

# print("✅ Dokument sačuvan u MongoDB!")