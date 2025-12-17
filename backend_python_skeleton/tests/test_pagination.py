from app.helpers.pagination import paginate, paginate_offset_limit

data = list(range(1, 51))  # sample data

print("Page-based pagination:")
print(paginate(data, page=2, page_size=10))

print("\nOffset-limit pagination:")
print(paginate_offset_limit(data, offset=10, limit=5))
