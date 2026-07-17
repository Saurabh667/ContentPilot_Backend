import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt
def save_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        uid = data.get("uid")
        name = data.get("name")
        email = data.get("email")
        photo = data.get("photo")

        user, created = User.objects.get_or_create(
            uid=uid,
            defaults={
                "name": name,
                "email": email,
                "photo": photo,
            }
        )

        return JsonResponse({
            "message": "User saved",
            "created": created
        })
    
    return JsonResponse({"error": "Only POST allowed"}, status=405)
