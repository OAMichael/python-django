from .models import FunctionGL, FunctionVK, Feedback

API_TYPE_GL = 0
API_TYPE_VK = 1

ADD_FUNCTION_SUCCESS = 0
ADD_FUNCTION_ALREADY_EXISTS = 1
ADD_FUNCTION_ERROR = 2


def get_api_suffix(api):
    if api == API_TYPE_GL:
        return "gl"
    elif api == API_TYPE_VK:
        return "vk"
    return None



def get_functions(api):
    db_entries = []
    if api == API_TYPE_GL:
        db_entries = FunctionGL.objects.all()
    elif api == API_TYPE_VK:
        db_entries = FunctionVK.objects.all()

    functions = []
    for entry in db_entries:
        functions.append([entry.signature, entry.description, entry.feature])

    return functions



def is_function_correct(signature, desc, feature):
    stripped = signature.strip()
    if len(stripped) == 0:
        return False

    stripped = desc.strip()
    if len(stripped) == 0:
        return False

    stripped = feature.strip()
    if len(stripped) == 0:
        return False

    return True


def add_function(username, email, signature, desc, feature, api):
    if is_function_correct(signature, desc, feature) == False:
        return ADD_FUNCTION_ERROR

    db_entries = []
    if api == API_TYPE_GL:
        db_entries = FunctionGL.objects.all()
    elif api == API_TYPE_VK:
        db_entries = FunctionVK.objects.all()

    if db_entries.filter(signature=signature).exists():
        return ADD_FUNCTION_ALREADY_EXISTS

    if email is None:
        email = ""

    db_entries.create(username=username, email=email, signature=signature, description=desc, feature=feature)
    return ADD_FUNCTION_SUCCESS



def get_statistics():
    stats = {
        "functions_gl_all": 0,
        "functions_gl_db": 0,
        "functions_gl_user": 0,
        "functions_gl_features": dict(),

        "functions_vk_all": 0,
        "functions_vk_db": 0,
        "functions_vk_user": 0,
        "functions_vk_features": dict(),
    }

    for entry_gl in FunctionGL.objects.all():
        stats["functions_gl_all"] += 1

        username = entry_gl.username
        if username is None or username == "":
            stats["functions_gl_db"] += 1
        else:
            stats["functions_gl_user"] += 1

        feature = entry_gl.feature
        gl_features = stats["functions_gl_features"]
        if feature in gl_features:
            gl_features[feature] += 1
        else:
            gl_features[feature] = 1

    for entry_vk in FunctionVK.objects.all():
        stats["functions_vk_all"] += 1

        username = entry_vk.username
        if username is None or username == "":
            stats["functions_vk_db"] += 1
        else:
            stats["functions_vk_user"] += 1

        feature = entry_vk.feature
        if feature in stats["functions_vk_features"]:
            stats["functions_vk_features"][feature] += 1
        else:
            stats["functions_vk_features"][feature] = 1

    return stats



def add_feedback(username, email, feedback):
    db_feedback = Feedback.objects.all()
    db_feedback.create(username=username, email=email, feedback=feedback)