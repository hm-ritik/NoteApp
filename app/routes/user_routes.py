from fastapi import APIRouter , HTTPException
from app.schemas.user_schema import UserCreate, UserResponse , UserUpdate
from app.services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_service,
     update_user_service,
     delete_user_service
)

router = APIRouter(prefix="/users", tags=["Users"])


# Create User
@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
   return await create_user_service(user)


# Get All Users
@router.get("/", response_model=list[UserResponse])
async def get_users():
    return await get_all_users_service()

#Get User 
@router.get("/{username}", response_model=UserResponse)
async def get_user(username: str):
    user = await get_user_service(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update User 

@router.put("/{username}", response_model=UserResponse)
async def update_user(username: str, user: UserUpdate):
    updated_user = await update_user_service(
        username,
        user.username,
        user.diary
    )
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{username}")
async def delete_user(username: str):

    deleted = await delete_user_service(username)

    if not deleted:
        raise HTTPException(status_code=404, detail="User Not Found")

    return {"message": "User deleted"}    
    
    

