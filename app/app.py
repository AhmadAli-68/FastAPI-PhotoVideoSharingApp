from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

posts = {
  1: {
      'title': 'Getting Started with Python',
      'content': 'Python is a beginner-friendly programming language with a simple and readable syntax.'
  },
    2: {
      'title': 'Understanding JavaScript',
      'content': 'JavaScript is widely used to build interactive and dynamic web applications.'
  },
  3: {
      'title': 'Learning TypeScript',
      'content': 'TypeScript adds static typing to JavaScript and helps developers write more maintainable code.'
  },
  4: {
      'title': 'What Is Git?',
      'content': 'Git is a version control system that helps developers track and manage changes in their projects.'
  },
  5: {
      'title': 'Introduction to APIs',
      'content': 'APIs allow different applications and services to communicate and exchange data.'
  },
  6: {
      'title': 'Understanding Databases',
      'content': 'Databases are used to store, organize, and retrieve application data efficiently.'
  },
  7: {
      'title': 'Building Your First Project',
      'content': 'Building projects is one of the best ways to turn programming knowledge into practical experience.'
  },
  8: {
      'title': 'Clean Code Matters',
      'content': 'Writing clean and readable code makes applications easier to understand, debug, and maintain.'
  },
  9: {
      'title': 'REST API Basics',
      'content': 'REST APIs commonly use HTTP methods such as GET, POST, PUT, and DELETE to work with resources.'
  },
  10: {
      'title': 'Keep Learning',
      'content': 'Consistent practice and solving problems regularly can help you become a stronger developer.'
    }
}

@app.get("/posts")
def get_posts(limit: int = None):
	if limit:
		return list(posts.values())[:limit]
	return posts

@app.get('/posts/{id}')
def get_post(id: int):
	if id not in posts:
		raise HTTPException(status_code=404, detail='Post not found')
	return posts.get(id)

@app.post('/posts')
def create_post(post: PostCreate) -> PostResponse:
	new_post = {'title': post.title, 'content': post.content}
	posts[max(posts.keys()) + 1] = new_post
	return new_post

@app.delete('/post/{id}')
def delete_post():
	pass