from mongoengine import Document, DateTimeField, ListField, ReferenceField, StringField

class Ranking(Document):
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'
    TIME_CHOICES = (
        (SHORT, 'Last 4 Weeks'),
        (MEDIUM, 'Last 6 Months'),
        (LONG, 'All Time')
    )

    ARTIST = 'artist'
    TRACK = 'track'
    TYPE_CHOICES = (
        (ARTIST, 'Artist'),
        (TRACK, 'Track')
    )

    timestamp = DateTimeField()
    type = StringField(choices=TYPE_CHOICES)
    time_range = StringField(choices=TIME_CHOICES)
    tracks = ListField(ReferenceField('Track'))
