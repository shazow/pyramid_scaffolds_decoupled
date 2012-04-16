An unofficial scaffolding for Pyramid. Recommended for advanced Pyramid or Pylons developers.

Highlights
==========

* Decoupled components: Use the project pieces independently of the web component.
* Inspired by the original Pylons project structure and the ``pyramid_routesalchemy`` paster template.
* Includes a reasonable CSS reset and an inheritance-based Mako template setup.
* SQLAlchemy-compatible but not setup out of the box.
* No hidden code in ``__init__.py`` files.
* All the web-related setup happens in ``{{project}}/web/environment.py``


Usage
=====

Install: ::

    $ pip install https://github.com/shazow/pyramid_scaffolds_decoupled/tarball/master
    $ pcreate --list
    Available scaffolds:
      alchemy:           Pyramid SQLAlchemy project using url dispatch
   -> pyramid_decoupled: Decouple web-specific code from the rest (models, library api, etc).
      starter:           Pyramid starter project
      zodb:              Pyramid ZODB project using traversal


Create a project: ::

    $ pcreate -s pyramid_decoupled foo
    $ cd foo
    $ find .
    ./CHANGES.txt
    ./MANIFEST.in
    ./README.txt
    ./development.ini
    ./production.ini
    ./foo
    ./foo/__init__.py
    ./foo/lib
    ./foo/lib/__init__.py
    ./foo/lib/helpers.py           <- Available as 'h' in templates.
    ./foo/models
    ./foo/models/__init__.py       <- Unopinionated model submodule.
    ./foo/tests
    ./foo/tests/__init__.py
    ./foo/web
    ./foo/web/__init__.py
    ./foo/web/environment.py       <- Setup like routes lives here.
    ./foo/web/static
    ./foo/web/static/css
    ./foo/web/static/images
    ./foo/web/static/js
    ./foo/web/templates
    ./foo/web/templates/base.mako
    ./foo/web/templates/index.mako
    ./foo/web/views
    ./foo/web/views/__init__.py
    ./foo/web/views/index.py
    ./setup.cfg
    ./setup.py


Start the server: ::

    $ python setup.py develop
    ... (Installs dependencies like pyramid-debugtoolbar, waittress, etc.)
    $ pserve development.ini 
    Starting server in PID 32481.
    serving on http://0.0.0.0:5000


Suggested Structure
-------------------

I'll usually build a context-insensitive API library in ``{{project}}/api/``, so
that I can do things like: ::

    >>> import foo.api
    >>> foo.api.account.change_password(user='foo', password='bar')
    >>> r = foo.api.inventory.list(limit=20)

The ``api`` generally uses the model to do things.

This way, most of the business logic lives in the API library and is easily used
by daemons, tests, or web views.


TODO
====

* Add pyramid.i18n.TranslationStringFactory stuff.
* Add an out-of-the-box SQLAlchemy setup
* Maybe add optional TurboMail example?
* Useful example for the api structure
* More documentation