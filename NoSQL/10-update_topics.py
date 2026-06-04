#!/usr/bin/env python3
"""Update topics of school documents."""


def update_topics(mongo_collection, name, topics):
    """Update all topics for schools matching name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
