from . import session, BASE_URL

class wmapi(object):
    def __init__(self,id):
        self._id = id

    def get_services(self):
        path = BASE_URL+'customers/{}/services'.format(self._id)
        response = session.get(path)
        return response.json()

    def get_planned_services(self):
        path = BASE_URL+'customers/{}/services/plan'.format(self._id)
        response = session.get(path)
        return response.json()

    def get_services_history(self):
        path = BASE_URL+'customers/{}/services/stats'.format(self._id)
        response = session.get(path)
        return response.json()
    
    def get_services_material(self):
        path = BASE_URL+'customers/{}/services/materials'.format(self._id)
        response = session.get(path)
        return response.json()

    def get_services_operation(self):
        path = BASE_URL+'customers/{}/services/operations'.format(self._id)
        response = session.get(path)
        return response.json()

    def get_services_price(self):
        path = BASE_URL+'customers/{}/services/prices'.format(self._id)
        response = session.get(path)
        return response.json()

    def get_service_ETA(self,serviceId):
        path = BASE_URL+'customers/{}/services/{0}/ETA'.format(self._id,serviceId)
        response = session.get(path)
        return response.json()
