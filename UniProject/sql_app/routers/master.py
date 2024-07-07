from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import master as crud
from datavalidation import valmaster
from schemas import master as schemas
from models import master as models
from dependencies import get_db

router=APIRouter()

@router.post("/createmaster/", response_model=schemas.master)
def create_master(pmaster: schemas.pmaster, db: Session = Depends(get_db)):
    valmaster.lid_check(pmaster.lid)
    valmaster.fname_check(pmaster.fname)
    valmaster.lname_check(pmaster.lname)
    valmaster.id_check(pmaster.id)
    valmaster.dep_check(pmaster.department)
    valmaster.major_check(pmaster.major)
    valmaster.birth_check(pmaster.birth)
    valmaster.born_check(pmaster.borncity)
    valmaster.address_check(pmaster.address)
    valmaster.postal_check(pmaster.postalcode)
    valmaster.cphone_check(pmaster.cphone)
    valmaster.hphone_check(pmaster.hphone)
    valmaster.lcid_check(pmaster.lcourseids)

    db_master = crud.get_master(db, lid=pmaster.lid)
    if db_master:
        raise HTTPException(status_code=400, detail="master already exists")
    master = crud.create_master(db, pmaster)
    return master

@router.get("/masters/{lid}", response_model=schemas.master)
def read_master(lid: str, db: Session = Depends(get_db)):
    master = crud.get_master(db, lid)
    if not master:
        raise HTTPException(status_code=404, detail="master not found")
    return master

@router.delete("/delmaster/{lid}")
def delete_master(lid: str, db: Session = Depends(get_db)):
    success = crud.delete_master(db, lid)
    if not success:
        raise HTTPException(status_code=404, detail="master not found")
    return {"detail": "master deleted successfully"}
    
@router.patch("/updatemaster/{lid}", response_model=schemas.master)
def update_master(lid: str, pmaster: schemas.masterupdate, db: Session = Depends(get_db)):
    valmaster.lid_check(pmaster.lid)
    valmaster.fname_check(pmaster.fname)
    valmaster.lname_check(pmaster.lname)
    valmaster.id_check(pmaster.id)
    valmaster.dep_check(pmaster.department)
    valmaster.major_check(pmaster.major)
    valmaster.birth_check(pmaster.birth)
    valmaster.born_check(pmaster.borncity)
    valmaster.address_check(pmaster.address)
    valmaster.postal_check(pmaster.postalcode)
    valmaster.cphone_check(pmaster.cphone)
    valmaster.hphone_check(pmaster.hphone)
    valmaster.lcid_check(pmaster.lcourseids)

    updated_master = crud.update_master(db=db, lid=lid, updated_data=pmaster)
    if updated_master is None:
        raise HTTPException(status_code=404, detail=f"master not found")
    return updated_master