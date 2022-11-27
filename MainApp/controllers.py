from MainApp.models import BoardGame, Purchase

def get_available_ads(req):
    ads = BoardGame.objects.filter(status=BoardGame.GameStatus.AVAILABLE)
    
    if req.user.is_authenticated:
        ads = ads.exclude(owner_id=req.user.id)
    return ads

def get_ads_from_user(user_id):
    ads = BoardGame.objects.filter(owner_id=user_id)
    return ads

def get_user_purchases(user_id):
    purchases = Purchase.objects.filter(buyer_id=user_id)
    return purchases
