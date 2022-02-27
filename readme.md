# StackOverflow RestfullAPI using Django

This is for test only 

### 1. Users:
### 1.1 Create User:
```bash
curl --location --request POST '/users/create/' \
--form 'password="password"' \
--form 'email="user email"' \
--form 'name="user name"'
```
### 1.2 Get Users:
```bash
curl --location --request GET '/users/'
```

### 2. Tags:
### 2.1 Create Tags:

```bash
curl --location --request POST '/tags/create/' \
--form 'name="tag name"'
```
### 2.1 Get Tags:

```bash
curl --location --request GET '/tags/'
```

### 3. Questions:
### 3.1 Create Question with multi tags:

```bash
curl --location --request POST '/questions/create/' \
--form 'title="the question title"' \
--form 'text="the question text will be here"' \
--form 'create_date="2022-02-02T19:00"' \
--form 'user="user_id"' \
--form 'tags="tag_id"' \
--form 'tags="tag_id"'
```

### 3.2 Get Questions with related data (comments, tags etc...):

```bash
curl --location --request GET '/questions/'
```

### 4. Answers:
### 4.1 Answer submitted questions:

```bash
curl --location --request POST '/answers/create/' \
--form 'text="the answer here"' \
--form 'create_date="2022-02-02T19:00"' \
--form 'user="user_id"' \
--form 'question="question_id"'
```
### 4.2 Get Answers:
```bash
curl --location --request GET '/answers/'
```

### 5. Comments:
### 5.1 Create Comment for Question:
```bash
curl --location --request POST '/comments/create/' \
--form 'text="this is a comment for Question 1"' \
--form 'user="1"' \
--form 'belong_to="1"' \
--form 'question="1"'
```

### 5.2 Create Comment for Answer:
```bash
curl --location --request POST '/comments/create/' \
--form 'text="this is a comment for answer 1"' \
--form 'user="1"' \
--form 'belong_to="2"' \
--form 'answer="1"'
```

### 5.2 GET Comments:
```bash
curl --location --request GET '/comments/' \
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)