from mainsite.models import Vendor

def vendor(request):
    if request.user.is_authenticated:
        if Vendor.objects.filter(profile_id = request.user.profile.id):
            return { 'vendor': Vendor.objects.get(profile_id = request.user.profile.id) }
        else:
            return { 'vendor': None }
    else:
        return { 'vendor': None }