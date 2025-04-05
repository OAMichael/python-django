from django.shortcuts import render
from django.core.cache import cache
from . import api_functions_work


def index(request):
    return render(request, "index.html")


def functions_list(request, api):
    functions = api_functions_work.get_functions(api)

    functions_list_html = "functions_list_"
    functions_list_html += api_functions_work.get_api_suffix(api)
    functions_list_html += ".html"

    return render(request, functions_list_html, context={"functions": functions})


def add_function(request, api):
    add_function_html = "add_function_"
    add_function_html += api_functions_work.get_api_suffix(api)
    add_function_html += ".html"

    return render(request, add_function_html)


def handle_add_function_result(result, context):
    if result == api_functions_work.ADD_FUNCTION_SUCCESS:
        context["result_title"] = "Success!"
        context["result_comment"] = "Thank you for providing a new function"
    elif result == api_functions_work.ADD_FUNCTION_ALREADY_EXISTS:
        context["result_title"] = "Already exists!"
        context["result_comment"] = "The function already in database"
    elif result == api_functions_work.ADD_FUNCTION_ERROR:
        context["result_title"] = "Failed!"
        context["result_comment"] = "Error occured while handling a function"


def send_function(request, api):
    if request.method == "POST":
        cache.clear()

        username = request.POST.get("username")
        email = request.POST.get("email")
        signature = request.POST.get("signature")
        desc = request.POST.get("desc")
        feature = request.POST.get("feature")

        result = api_functions_work.add_function(username, email, signature, desc, feature, api)

        context = {
            "gl_const": api_functions_work.API_TYPE_GL,
            "vk_const": api_functions_work.API_TYPE_VK
        }

        context["username"] = username
        context["api"] = api
        handle_add_function_result(result, context)

        return render(request, "send_function.html", context)
    else:
        return add_function(request, api)


def statistics(request):
    stats = api_functions_work.get_statistics()
    return render(request, "statistics.html", stats)


def feedback(request):
    return render(request, "feedback.html")


def send_feedback(request):
    if request.method == "POST":
        cache.clear()

        username = request.POST.get("username")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")

        api_functions_work.add_feedback(username, email, feedback)

        context = {"username":  username}
        return render(request, "send_feedback.html", context)
    else:
        return feedback(request)