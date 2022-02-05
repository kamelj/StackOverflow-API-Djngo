# StackOverflow RestfullAPI using Django

This is for test only 

## Documentation

Use the link here to access the API [http://localhost:88](http://localhost:88/)

### 1. Create User:

```bash
curl --location --request POST 'http://localhost:88/users/create/' \
--form 'password="password"' \
--form 'email="user email"' \
--form 'name="user name"'
```

### 2. Create Tag:

```bash
curl --location --request POST 'http://localhost:88/tags/create/' \
--form 'name="tag name"'
```

### 3. Create Question with multi tags:

```bash
curl --location --request POST 'http://localhost:88/questions/create/' \
--form 'title="the question title"' \
--form 'text="the question text will be here"' \
--form 'create_date="2022-02-02T19:00"' \
--form 'user="user_id"' \
--form 'tags="tag_id"' \
--form 'tags="tag_id"'
```

### 4. Create answer for a question:

```bash
curl --location --request POST 'http://localhost:88/answers/create/' \
--form 'text="the answer here"' \
--form 'create_date="2022-02-02T19:00"' \
--form 'user="user_id"' \
--form 'question="question_id"'
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)