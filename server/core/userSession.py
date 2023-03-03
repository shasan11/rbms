from threading import local
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin

 
_user = local()

 
class CurrentUserMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        try:
            _user.value = request.user
            _user.branch=request.user.branch
            _user.branch_id=request.user.branch.id
        except:
            pass
 
def get_current_user():
    try:
        return _user.value
    except AttributeError:
        return None
    except:
        return None
    
def get_current_user_branch():
    try:
        return _user.branch
    except AttributeError:
        return None
    except:
        return None

def get_current_user_branch_id():
    try:
        return int(_user.branch_id)
    except AttributeError:
        return None
    except:
        return None