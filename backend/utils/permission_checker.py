from fastapi import Depends, HTTPException
from utils.jwt_handler import get_current_user
from 

def require_permission(permission):

    def checker(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
    ):

        role_id = current_user.role_id

        permission_exists = db.query(RolePermission)\
            .join(Permission)\
            .filter(
                RolePermission.role_id == role_id,
                Permission.name == permission
            ).first()

        if not permission_exists:
            raise HTTPException(status_code=403)

        return current_user

    return checker