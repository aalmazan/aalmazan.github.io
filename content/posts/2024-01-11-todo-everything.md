Title: TODO: Everything
Date: 2024-01-11
Modified: 2024-01-11
Status: published
Category: projects
Tags: todo-everything, programming
Slug: todo-everything-begins
Summary: What the TODO: Everything project is and why.
---

New year, more personal projects to procrastinate on.

A few years ago I thought an idea called "TODO Everything" which can be summed up as "The TODO app that does
everything." I had ideas of grandeur where it would have every feature imaginable; integrate a bunch of different
services; _be_ a bunch of different services; have complex backend systems that would do anything you need. It's an
insane idea, and I always loved thinking
about it. Essentially, it's something like a "Scope Creep Simulator", or maybe the absolute opposite of
what [code golf](https://en.wikipedia.org/wiki/Code_golf) is.

The purpose of Todo apps is pretty simple: people need toy/example/test apps to build, especially when learning a new
language/framework/platform/etcetera. In the web app world there's a few that come to mind: blogs, social media clones,
and Todo apps. Essentially, they're just [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) apps with
a database (or some type of data storage) that can maybe have multiple users and maybe a few actions can be done (i.e.
completing a Todo item, or liking a post). That's it.

Of course, you'd want the scope to be minimal since you're just learning your shiny new language or tool, but it can get
exponentially more interesting when you silence your inner _Project Manager/Lead Developer_ and tell yourself, "You know
what? We _can_ add a few more weeks to this feature in order to get it working on a local Kubernetes cluster running on
your Raspberry Pis."

So, a month or so ago that's what I did. I've engineered myself into corners and bulldozed those walls to create even
more corners, but it has been interesting and mostly fun to work on. Will this be a major start up that will change
people's lives for the better and solve global healthcare? No. 99.999% guaranteed to do nothing, but some learning's
getting done, maybe it'll help other people as well.

I've created the GitHub organization [todo-everything](https://github.com/todo-everything) that will house everything
"TODO: Everything" (actual "real" name not confirmed). So far the following are up in mostly working condition with an
infinity of features left to go.

* Backend written in Python + Django. Mainly using Django for its ORM
  and [`django-rest-framework`](https://www.django-rest-framework.org/)
    * https://github.com/todo-everything/todo-everything-django
* A frontend written in TypeScript using [SolidJS](https://www.solidjs.com/) and [Vite](https://vitejs.dev/) (
  the `solid-ts` vite template). This was written first to get a feel for
  the API. Probably should be written later, but that's a story for a different post.
    * https://github.com/todo-everything/todo-everything-solid
* Another frontend written TypeScript using [React](https://react.dev/), [SWC](https://swc.rs/) and
  also [Vite](https://vitejs.dev/) (`react-swc-ts` template).
    * https://github.com/todo-everything/todo-everything-react
* Everything OPs related. So far just some Ansible and Kubernetes files, but it also supports ARM because of Raspberry
  Pis.
    * https://github.com/todo-everything/todo-everything-ops

I've learned more in the past few months than I have even in some other jobs since it's completely void of any
"business" and "logic". At least for now. Hah, but no this will almost never be a viable business idea. I do have a
feature idea for `todo-everything`, though, that would integrate Stripe (initially) charge a user a metered rate for
each Todo item the create and complete. Another very wild idea, but I think I've actually seen a variant of that on an
existing iOS Todo app... Future post ideas are abundant, but that's the end of this one for now.

Dreaming big and making my backlog infinite when time is very much limited. This is 2024.