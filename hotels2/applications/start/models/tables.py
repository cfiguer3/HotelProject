#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

from datetime import datetime

#table for user posts
db.define_table('Hotels',
                Field('Name', 'text', required=True),
                Field('Phone_number', required=True),
                Field('Available_rooms', 'integer', default=0, requires=IS_INT_IN_RANGE(0, 500)),
                Field('Address', 'text', required=True),
                Field('Description', 'text'))

db.define_table('Bedroom',
                Field('room_id', readable=False, writable=False),
                Field('Beds', 'integer'),
                Field('Availability', 'boolean'),
                Field('DateStart', 'datetime'),
                Field('DateEnd', 'datetime'),
                Field('Price'),
                Field('Description', 'text'),
                Field('Hotel_ID', 'reference Hotels', readable=False, writable=False),
                Field('reservation', 'datetime'),
                Field('wifi', 'boolean'),
                Field('standard_breakfast', 'boolean'),
                Field('cable', 'boolean'),
                Field('premium_breakfast', 'boolean'),
                Field('lunchAndDinner', 'boolean'))

db.define_table('Dates',
                Field('DateStart', 'datetime', requires=IS_DATE),
                Field('DateEnd', 'datetime', requires=IS_DATE),)

db.define_table('Amenities',
                Field('wifi', 'integer'),
                Field('standard_breakfast', 'integer'),
                Field('cable', 'integer'),
                Field('premium_breakfast', 'integer'),
                Field('lunchAndDinner', 'integer'),
                Field('Bed', 'reference Bedroom'))

db.define_table('Patron',
                Field('Address', 'text', required=True),
                Field('City', 'text', required=True),
                Field('Zip', 'integer', requires=IS_INT_IN_RANGE(5, 5)),
                Field('CreditCardNum', 'integer', requires=IS_INT_IN_RANGE(16, 16))
                )

db.Bedroom.DateStart.default = datetime.utcnow()
db.Bedroom.DateEnd.default = datetime.utcnow()
