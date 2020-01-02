from wmapi import wmapi

customerId = filter_query_parameters=['customerId']
serviceId = filter_query_parameters=['serviceId']

def test_services():
    """Tests an API call to get services"""
    wmapi_instance = wmapi(customerId)
    response = wmapi_instance.get_services()
    assert isinstance(response,dict)

def test_planned_services():
    """Tests an API call to get planned services"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_planned_services()
    assert isinstance(response, dict)

def test_services_history():
    """Tests an API call to get services history"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_services_history()
    assert isinstance(response, dict)

def test_services_material():
    """Tests an API call to get services marerial"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_services_material()
    assert isinstance(response, dict)

def test_services_operation():
    """Tests an API call to get services operation"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_services_operation()
    assert isinstance(response, dict)

def test_services_price():
    """Tests an API call to get services price"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_services_price()
    assert isinstance(response, dict)

def test_service_ETA():
    """Tests an API call to get service ETA"""
    wmapi_instance  = wmapi(customerId)
    response = wmapi_instance.get_service_ETA(serviceId)
    assert isinstance(response, dict)