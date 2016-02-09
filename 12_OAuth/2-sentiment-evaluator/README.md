Twitter Sentiment Evaluator
===========================

Using your project that allows for Twitter authorization, create a simple sentiment evaluator module for Tweets.

Give the User a form that lets them search Twitter for a hashtag. The list of tweets it receives back should be parsed through
your sentiment evaluator, and return whether the general opinion on that hashtag is positive or negative.

Display something to the user like this:

"From a sample size of N Tweets, people tweeted X amount of positive keywords and X amount of negative keywords. The general feelings towards this hashtag are [Positive|Negative]"

Use the following word lists - if you want to add your own, do so.
```py
positive = ['love','loved','like','liked','awesome','amazing','good','great','excellent', 'nice', 'sweet']

negative = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst', 'disgraceful', 'horrible']
```
