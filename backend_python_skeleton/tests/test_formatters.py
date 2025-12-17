from app.helpers.formatters import (
    success_response,
    error_response,
    format_list,
    format_single
)

users = [
    {"id": 1, "name": "Alice", "email": "a@test.com", "password": "hidden"},
    {"id": 2, "name": "Bob", "email": "b@test.com", "password": "hidden"},
]

print(success_response("Operation completed"))
print(error_response("Invalid request", 400))

print("\nFormatted list:")
print(format_list(users, ["id", "name"]))

print("\nFormatted single:")
print(format_single(users[0], ["id", "email"]))
