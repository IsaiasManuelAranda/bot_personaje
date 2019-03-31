import web
import config

db = config.db


def get_all_personaje():
    try:
        return db.select('personaje')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_personaje(id_personaje):
    try:
        return db.select('personaje', where='id_personaje=$id_personaje', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_personaje(id_personaje):
    try:
        return db.delete('personaje', where='id_personaje=$id_personaje', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_personaje(nombre_personaje,descripcion):
    try:
        return db.insert('personaje',nombre_personaje=nombre_personaje,
descripcion=descripcion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_personaje(id_personaje,nombre_personaje,descripcion):
    try:
        return db.update('personaje',id_personaje=id_personaje,
nombre_personaje=nombre_personaje,
descripcion=descripcion,
                  where='id_personaje=$id_personaje',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
