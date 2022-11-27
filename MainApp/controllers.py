from MainApp.models import BoardGame

def get_available_ads(req):
    ads = BoardGame.objects.filter(status=BoardGame.GameStatus.AVAILABLE)
    
    if req.user.is_authenticated:
        ads = BoardGame.objects.exclude(owner_id=req.user.id)
    return ads

def get_ads_from_user(user_id):
    ads = BoardGame.objects.filter(owner_id=user_id)
    return ads