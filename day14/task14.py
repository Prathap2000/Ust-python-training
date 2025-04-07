def requires_admin(func):
    def wrap(*agrs,**kagrs):
        if dict(kagrs) ['user_role']!="admin":
            print("Access Denied,Login as admin")
            return None
        else:
            return func(*agrs,**kagrs)
    return wrap
   
@requires_admin
def delete_data(user_role):
    print("Data deleted.")

delete_data(user_role="admin")      # Allowed
delete_data(user_role="guest")