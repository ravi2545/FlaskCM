from datetime import date
from pprint import pprint


from marshmallow import Schema, fields

class ArtistSchema(Schema):
    # name is a variable withe the reference string datatype which is string fields in marshmallow
    name = fields.Str()



class AlbumSchema(Schema):
    title = fields.Str()
    # release_date is a date datatype and fields type in marshmallow
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


Sanaboina = dict(name='Ravi Prasad Sanabaoina')
album = dict(artist=Sanaboina, title='I am simple', release_date=date(1971, 12, 17))


schema = AlbumSchema()
result = schema.dump(album)
rs = pprint(result, indent=2)