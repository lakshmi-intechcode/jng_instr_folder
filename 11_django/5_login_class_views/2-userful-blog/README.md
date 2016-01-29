Userful Blog
============

Using the Userless Blog you just built, and your user module from this week, create a blog that allows multiple users to sign up, sign in, and write posts. An unauthenticated user should not be able to create posts.

This is an open-ended challenge. You will need to be creative to build this out efficiently. Plan your steps as you go.

#### The Main Page

The main page of the blog should display all posts, by all users, ordered by most recent first.

Think about user experience! It should display the the linked title, some preview of the content inside, when it was posted and the user who posted it.

#### The User Page

Going to a the user page - something like `mysweetblog.com/<username>` should show the exact same template as the home page - except it should only be that specific users blog posts.

#### Comments

Add comments to posts. A comment should belong to a User and to a Post.

All of a post's comments should display beneath it's content. What is the DRY way to do this in the template?

#### Nested Comments

Add comments to comments! A user should be able to reply to a comment, and have it displayed below.

The best way to do this is with a [Generic Relation](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#generic-relations) in comments. For reference, this is sometimes called a Polymorphic Association.

Make sure that you edit the css so that a nested comment's div is clearly indented below its parent.

This is tough - you'll need to think algorithmically. Make a plan.
