from app.models import User, Link, Like
from app import db

u1 = User(username='Alan', email='a@g.com', password='!#"123')
u2 = User(username='Peter', email='p@b.com', password='!#"123')
u3 = User(username='John', email='j@b.com', password='!#"123')

print(u1)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)

# db.session.commit()

l1 = Link(
    title='Data Structures',
    user_id= u1.id,
    description="Data structures are basic building blocks of any software program. The few most common data structures are array, linked list, tree, stack, queue, etc. In this series, you will understand what data structures are and their implementations in different programming languages.",
    url='https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12',
    image_url='https://i.ytimg.com/vi/Qmt0QwzEmh0/hq720.jpg?sqp=-oaymwEXCK4FEIIDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAYZvp1_7HVUd7kk9mRYfTfNswGag'
)
l2 = Link(
    title='PostgreSQL Tutorial',
    user_id= u1.id,
    description="Learn how to use PostgreSQL in this full course. PostgreSQL is a general purpose and object-relational database management system. It is the most advanced open source database system widely used to build back-end systems.",
    url='hhttps://www.youtube.com/watch?v=qw--VYLpxG4',
    image_url='https://kinsta.com/wp-content/uploads/2022/04/postgres-logo.png'
)
db.session.add(l1)
db.session.add(l2)

li1 = Like(
    user_id= u2.id,
    link_id= l1.id
)
li2 = Like(
    user_id= u3.id,
    link_id= l1.id
)
db.session.add(li1)
db.session.add(li2)

db.session.commit()
