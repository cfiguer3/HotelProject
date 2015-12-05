# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################


def hotelrooms():
    entry = db.Hotels(request.args(0))
    Admins = ["manager@gmail.com"]
    form = SQLFORM(db.Bedroom)
    form2 = SQLFORM(db.Dates)
    form.vars.Hotel_ID = request.args(0)
    form.add_button('Cancel', URL('default', 'index'))
    if form.process().accepted:
        session.flash = T('data was inserted')
        redirect(URL('default', 'hotelrooms', args=entry.id))
    elif form.errors:
        response.flash = 'form has errors'

    q = db.Bedroom.Hotel_ID == request.args(0)
    query = db(q).select(db.Bedroom.ALL)

    return dict(entry=entry, query=query, q=q, form=form, Admins=Admins, form2=form2)


def checkout():

    return dict()


def default():
    return dict()


def homepage():
    form = SQLFORM(db.Hotels)
    form.add_button('Cancel', URL('default', 'index'))
    if form.process().accepted:
        session.flash = T('data was inserted')
        redirect(URL('default', 'index'))
    elif form.errors:
        response.flash = 'form has errors'
    hotel_list = db(db.Hotels).select(orderby=db.Hotels.Name)
    return dict(hotel_list=hotel_list, form=form)


def index():
    Admins = ["manager@gmail.com"]
    form = SQLFORM(db.Hotels)
    form.add_button('Cancel', URL('default', 'index'))
    if form.process().accepted:
        session.flash = T('data was inserted')
        redirect(URL('default', 'index'))
    elif form.errors:
        response.flash = 'form has errors'
    hotel_list = db(db.Hotels).select(orderby=db.Hotels.Name)

    return dict(hotel_list=hotel_list, form=form, Admins=Admins)


def load_hotels():
    """loads all hotels for the page"""
    rows = db(db.Hotels).select()
    d = {}
    for r in rows:
        d[r.id] = {'Name': r.Name,
                   'Phone_number': r.Phone_number,
                   'Available_rooms': r.Available_rooms,
                   'Address': r.Address,
                   'Description': r.Description}
    return response.json(dict(Hotel_list=d))


def user():

    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def refresh():
    db(db.Hotels.id > 0).delete()
    redirect(URL('default', 'index'))
    return dict()

