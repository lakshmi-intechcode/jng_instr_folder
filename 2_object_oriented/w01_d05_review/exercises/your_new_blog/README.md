Your New Blog
==============

Jekyll is a fantastic website generator and framework that's designed to build minimal static blogs to be hosted on GitHub pages. It provides you with a boilerplate template of how a blog can be set up. 

This weekend you're going to install, set-up, make a small post, and deploy your own blog!

You'll need Ruby to run jekyll. Follow the directions on the front page [here](https://rvm.io/) to install Ruby. 

### Installation/Setup
  - Open up your terminal and run:
        ```
        gem install jekyll
        ```
  - Create a new boilerlate website using the command:
        ```
        jekyll new {{INSERT SITE NAME HERE}}
        ```
  - Build and serve your new blog
        ```
        jekyll serve
        ```
  - Open your browser && go to address served in terminal

### Write a post!
  - Navigate to `_post/`
  - Create a new file with the format of: `YYYY-MM-DD-name-of-post.extension`
  - Include && edit the config at top of page to reflect your current page

### Deployment
As a GitHub user, you're entitled to one free "user" website, which will live at `http://yourusername.github.io`. 

 - Create a new PUBLIC repo
 - Name the repo 'yourusername.github.io' replacing yourusername with your GitHub username (!!!!!)
 - Initialize this project with a README and add an MIT license
 - Clone your newly created repo to your machine
 - Push your Jekyll blog on the master branch of this repo


### Resources:
  - Free [themes](http://jekyllthemes.org/)
    - To install, download, config, && serve
  - Jekyll [docs](http://jekyllrb.com/docs/home/)
