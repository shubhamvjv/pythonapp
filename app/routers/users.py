from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
