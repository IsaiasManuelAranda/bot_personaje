import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_personaje, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_personaje) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_personaje, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_personaje) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_personaje, **k):

    @staticmethod
    def POST_DELETE(id_personaje, **k):
    '''

    def GET(self, id_personaje, **k):
        message = None # Error message
        id_personaje = config.check_secure_val(str(id_personaje)) # HMAC id_personaje validate
        result = config.model.get_personaje(int(id_personaje)) # search  id_personaje
        result.id_personaje = config.make_secure_val(str(result.id_personaje)) # apply HMAC for id_personaje
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_personaje, **k):
        form = config.web.input() # get form data
        form['id_personaje'] = config.check_secure_val(str(form['id_personaje'])) # HMAC id_personaje validate
        result = config.model.delete_personaje(form['id_personaje']) # get personaje data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_personaje = config.check_secure_val(str(id_personaje))  # HMAC user validate
            id_personaje = config.check_secure_val(str(id_personaje))  # HMAC user validate
            result = config.model.get_personaje(int(id_personaje)) # get id_personaje data
            result.id_personaje = config.make_secure_val(str(result.id_personaje)) # apply HMAC to id_personaje
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/personaje') # render personaje delete.html 
