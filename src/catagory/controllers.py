from fastapi import status,HTTPException
from sqlalchemy.orm import Session 
from .dtos import CatagorySchema
from .models import CatagoryModel
from src.user.models import UserModel

def get_all(db:Session):
    data= db.query(CatagoryModel).all()

    return data

def get_one(catagories_id: int, db:Session):
    data= db.query(CatagoryModel).get(catagories_id)

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return data

def create(body:CatagorySchema, db:Session, user:UserModel):
    if user.is_admin:
        data=CatagoryModel(
        name=body.name,
        description=body.description
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

def update(catagories_id:int, body:CatagorySchema, db:Session, user:UserModel):
    if user.is_admin:
        instance= db.query(CatagoryModel).get(catagories_id)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        new_data=body.model_dump()

        for key,val in new_data.items():
            setattr(instance, key, val)

        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

    

def delete_catagory(catagories_id:int, db:Session, user:UserModel):
    if user.is_admin:
        data= db.query(CatagoryModel).get(catagories_id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        db.delete(data)
        db.commit()
        

        return None

    