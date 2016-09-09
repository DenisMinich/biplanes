"""Tag implementation"""

from collections import defaultdict


class Tag(object):
    """Collects tags and assigned objects"""

    tags = defaultdict(set)
    """Dict with key as tag and list of assigned objects"""

    @staticmethod
    def add_tag(instance, tag):
        """Assign object with tag"""
        if instance not in Tag.tags[tag]:
            Tag.tags[tag].add(instance)

    @staticmethod
    def remove_tag(instance, tag):
        """Unassign object with tag"""
        if instance in Tag.tags[tag]:
            Tag.tags[tag].remove(instance)
