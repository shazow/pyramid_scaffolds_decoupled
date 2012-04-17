"""SQLAlchemy Metadata and Session object"""
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


__all__ = ['Session', 'metadata', 'BaseModel']


# Remove expire_on_commit=False if autorefreshing of committed objects is
# desireable.
Session = scoped_session(sessionmaker(expire_on_commit=False))
metadata = MetaData()


# Declarative base

from sqlalchemy.ext.declarative import declarative_base

class _Base(object):
    @classmethod
    def get(cls, id):
        return Session.query(cls).get(id)

    @classmethod
    def get_by(cls, **kw):
        return Session.query(cls).filter_by(**kw).first()

    @classmethod
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)
        if r:
            return r

        return cls.create(**kw)

    @classmethod
    def create(cls, **kw):
        r = cls(**kw)
        Session.add(r)
        return r

    @classmethod
    def insert(cls, **kw):
        Session.execute(cls.__table__.insert(values=kw)).close()

    @classmethod
    def insert_many(cls, iter):
        Session.execute(cls.__table__.insert(), list(iter)).close()

    @classmethod
    def all(cls):
        return Session.query(cls).all()

    def delete(self):
        Session.delete(self)

    def refresh(self):
        Session.refresh(self)

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in self.__table__.c.keys())
        return "%s(%s)" % (self.__class__.__name__, values)


BaseModel = declarative_base(metadata=metadata, cls=_Base)
