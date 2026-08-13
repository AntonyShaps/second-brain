# In the very end you will find what I have started with.(Marked with [initial-documentation])
## Purpose of this documentation

These kind of documentation is created to be comfortable for me. Do not take it seriously, it may not follow commonly acceted principles or rules.

## Logs on app development process

1. First try lead to rathe fast understanding that i need some knowledge on DDD, as i had never designed full system groun up and at some point you start hitting some kind of block. You understand how isolated elements work, but you can't put them together. Why DDD? Because I have tried to finish 'cosmic python' several times, but found the language of Domain-Driven-Desing very abstract and hard to contemplate, but as soon as I hit a wall with this app - there was no other choice for me, but i needed to take longer path. And actually can recommened the following two books: [link1], [link2]. What I figured out is that - yes, this is very hard "language", but you start to wrap you head around it the more you think about it, especially in relation to your app. Mapping concepts mentioned in literature helps a lot. Additionally, there are no set in stone rules and its up to you to decide how actually to desing your application as DDD gives you just a set of tools, which helps to bring those "isolated elements" together in an efficient way, and you are free to choose the ones which you deem useful in your case.

2. In my case I decide to follow TDD on purpose, because i believe this approach creates higher quality software. I was lucky to discover a technique called scenarios from godfather of DDD - [Name, Surname]. Honestly, I was just shocked how stupid I am, but there is really no magic here, you just create scenarios. And it perfectly fits TDD, because your scenarios can become your tests. Its hard to explain in words, but I think every person who decided to desing their app ground up for the first time faces this issue. You kinda now a lot, but do not know how and where to start and even such simple things as scenarios, which you can come up with by yourself, are just missing from your mind for some reason.

### Scenario [Todos]



[initial-documentation]
Disclaimer: Below is just a dump from all files which i used to have in the very begining. I realised rather quickly that: 1. I really do not need such a big amount of documentation. 2. I lack experience and knowledge on how to desing an app ground up.


# Application vision

## Problematics

Currently I do not feel comfortable using different applications for basically managing my life. Some feel too cumbersome, some to shallow, the aim of this application is to create a "platform", where I can manage my life eifficiently in one place.

## Planned functionality

The initial functions I'd like to have:

- Todo lists
- Time blocking
- Calendar view
- Knowledge base
- Flash cards
- Note taking
- Project views

## First TODO

1. Having first CRUD app as fast as possible
2. Actually needed to take a step back, to switch to Domain modelling
3. Read through two books on DDD - figure out next steps

# ADR-01: initial design thoughts

Decisions:
Use FastAPI and React for development.
Do not focus on data model too much as of now.

Reasons:
Faster development due to familiarity with FastAPI and React. 
Have been thinking about it for a while already and have not find optimal one yet.

Consequences:
Faster MVP.
Issues with data model guaranteed...

# ADR-02: db selection

Decisions:
Use SQLite as db

Reasons:
Lightweight, easy to setup

Consequences:
Faster MVP but may require migration to another if scaling issue arise(highly unlikely)

# ADR-03: start with React development

Decisions:
switching to React frontend development without isolated temporary SQLlite db for tests 

Reasons:
Faster iteration between frontend and backend to get first iteration of APP readily running on the server

Consequences:
Again trading off quality for speed, but in restricted timeframe it is more optimal and I still will be back to test DB later

# ADR-04: Step back to take a look at domain-driven-design

Decisions:
Stop and focus more time on designing the app

Reasons:
Stumbled upon data modelling multiple times and couldn't understand where to start

Consequences:
More time spend on understanding DDD, ports and adapters, repositories but I will have a lot clearer picture in my mind
