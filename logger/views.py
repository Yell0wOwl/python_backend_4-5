from django.shortcuts import render, get_object_or_404, redirect

from functools import wraps

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST

from .models import Message
from .serializers import MessageSerializer

def custom_login_required():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                req = list(request.get_renderer_context().values())[3]
            except AttributeError:
                req = request
            if req.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/login/')
        return wrapper
    return decorator


def login(request):
    return render(request, 'login.html')

@custom_login_required()
def index(request):
    return render(request, 'log_index.html')

class MessageViewSet(viewsets.ViewSet):

    @custom_login_required()
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @custom_login_required()
    def retrieve(self, request, pk=None):
        queryset = Message.objects.all()
        msg = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(msg)
        return Response(serializer.data)

    @custom_login_required()
    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    @custom_login_required()
    def update(self, request, pk=None):
        queryset = Message.objects.all()
        msg = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(instance=msg, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

    @custom_login_required()
    def destroy(self, request, pk=None):
        queryset = Message.objects.all()
        msg = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(msg)
        msg.delete()
        return Response(serializer.data)

# @require_GET
# def msg_info(request, id):
#     queryset = Message.objects.all()
#     msg = get_object_or_404(queryset, pk=id)
#     return JsonResponse(
#         {
#             'id': msg.id,
#             'companion': msg.companion_id,
#             'text': msg.msg_text,
#         }
#     )

# @require_POST
# def msg_create(request, companion_id = None):
#     msg_text = request.POST.get('text')
#     new_msg = Message.objects.create(user_id='0', companion_id=companion_id, msg_text=msg_text, msg_time=None)
#     return JsonResponse(
#         {
#             'New message':
#                 {
#                     'id': new_msg.id,
#                     'companion': new_msg.companion_id,
#                     'text': new_msg.msg_text,
#                 }
#         }
#     )

# @require_GET
# def msg_list(request):
#     msgs = Message.objects.all()
#     data = [
#         {
#             'id': msg.id,
#             'companion': msg.companion_id,
#             'text': msg.msg_text,
#         } for msg in msgs
#     ]
#     return JsonResponse({'Messages': data})
#
# @require_POST
# def msg_delete(request, id):
#     queryset = Message.objects.all()
#     msg = get_object_or_404(queryset, pk=id)
#     mid = msg.id
#     mcid = msg.companion_id
#     mtxt = msg.msg_text
#     msg.delete()
#     return JsonResponse(
#         {'Deleted':
#             {
#                 'id': mid,
#                 'companion': mcid,
#                 'text': mtxt,
#             }
#         }
#     )
#
# @require_POST
# def msg_change(request, id):
#     new_id = request.POST.get('id')
#     new_text = request.POST.get('text')
#     new_time = request.POST.get('time')
#     queryset = Message.objects.all()
#     msg = get_object_or_404(queryset, pk=id)
#     if not(new_id is None):
#         msg.companion_id = new_id
#     if not(new_text is None):
#         msg.msg_text = new_text
#     if not(new_time is None):
#         msg.msg_time = new_time
#     msg.save()
#     return JsonResponse({'Updated':
#             {
#                 'ID': msg.companion_id,
#                 'Text': msg.msg_text,
#                 'Time': msg.msg_time,
#             }
#     }
#     )