from app.database import user_collection
from app.models.user_model import user_helper


# Create User
async def create_user_service(user_data):

    # Check if username exists
    existing_user = await user_collection.find_one(
        {"username": user_data.username}
    )

    if existing_user:
        return None

    # Insert user
    user_dict = user_data.dict()

    result = await user_collection.insert_one(user_dict)

    new_user = await user_collection.find_one(
        {"_id": result.inserted_id}
    )

    return user_helper(new_user)



# Get All Users
async def get_all_users_service():

    users = []

    async for user in user_collection.find():

        users.append(user_helper(user))

    return users
# Get User 

async def get_user_service(username:str):
    user= await user_collection.find_one({'username':username})
    if user:
        return user_helper(user)
    return None

# Update User 

async def update_user_service(old_username: str, new_username: str, diary: str):
    user = await user_collection.find_one({'username': old_username})
    if user:
        await user_collection.update_one(
            {"username": old_username},
            {"$set": {"username": new_username, "diary": diary}}
        )
        updated_user = await user_collection.find_one(
            {"username": new_username}
        )

        return user_helper(updated_user)

    return None

#Delete User
async def delete_user_service(username:str):
    user=await user_collection.find_one({'username': username})
    if user:
        await user_collection.delete_one({'username':username})
        return True
    return False
             
           
       
        

        
        
