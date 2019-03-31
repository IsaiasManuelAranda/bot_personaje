import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_personaje, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_personaje) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_personaje, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_personaje) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_personaje, **k):

    @staticmethod
    def POST_EDIT(id_personaje, **k):
        
    '''

    def GET(self, id_personaje, **k):
        message = None # Error message
        id_personaje = config.check_secure_val(str(id_personaje)) # HMAC id_personaje validate
        result = config.model.get_personaje(int(id_personaje)) # search for the id_personaje
        result.id_personaje = config.make_secure_val(str(result.id_personaje)) # apply HMAC for id_personaje
        return config.render.edit(result, message) # render personaje edit.html

    def POST(self, id_personaje, **k):
        form = config.web.input()  # get form data
        form['id_personaje'] = config.check_secure_val(str(form['id_personaje'])) # HMAC id_personaje validate
        # edit user with new data
        result = config.model.edit_personaje(
            form['id_personaje'],form['nombre_personaje'],form['descripcion'],
        )
        if result == None: # Error on udpate data
            id_personaje = config.check_secure_val(str(id_personaje)) # validate HMAC id_personaje
            result = config.model.get_personaje(int(id_personaje)) # search for id_personaje data
            result.id_personaje = config.make_secure_val(str(result.id_personaje)) # apply HMAC to id_personaje
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/personaje') # render personaje index.html
