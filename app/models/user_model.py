def user_helper(user):

    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "diary": user["diary"]
    }

def note_helper(note):
    return{
        "id":str(note["_id"]),
        "note":note
    }