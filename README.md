# Django Portfolio App
 I made own portfolio web site which containts cv/resume, blog page, projects page and contact.


## Main Page
- I added navbar in base.html for access every html files.
- I added my cv, skills, accounts etc.
- I used bootstrap in front-end

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/main1.jpg)

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/main2.jpg)

## Blog Page 
- I used django featues to create blog app
- I displayed all posts with generic listview

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/blog1.jpg)

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/blog2.jpg)

>Also you can display article 
![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/blog3.jpg)

### Sign up & Sign in

- I used django user.auth feature for register and login.
- Also i used crispy-forms module to make the forms look more beautiful. 
- I used messages module when the form is invalid.

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/signup.jpg)

### Profile
- The user able to see own posts.
- And able to change own about section.

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/profile.jpg)

### Publishing Post
-The user able to publish own posts on this form.
-I used ckeditor module for editing blog content.


![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/publishpost.jpg)


## Contact Page
- I added my contact info.
- I used mapbox plugin to display my locaiton.

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/contact.jpg)

## Projects Page

-I added my projects and showed as card in this page.

![](https://github.com/uberfresh/djangoPortfolio/blob/main/screenshots/projects.jpg)

## Requirements and Usage
- Pull request this repo
- Create own venv
- Install requirements
```
$ pip install requirements.txt
```
- Run the server and done!
```
python manage.py runserver
```






