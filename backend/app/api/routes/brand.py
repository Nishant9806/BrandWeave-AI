from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Organization, BrandFact, BrandTerm, BrandGuideline

router = APIRouter()


def get_demo_organization(db: Session):
    organization = (
        db.query(Organization)
        .filter(Organization.name == "TechNova")
        .first()
    )

    if not organization:
        raise HTTPException(
            status_code=404,
            detail="Brand organization not found. Please seed the database."
        )

    return organization


@router.get("/brand")
def get_brand_profile(db: Session = Depends(get_db)):
    organization = get_demo_organization(db)

    return {
        "id": str(organization.id),
        "name": organization.name,
        "product_name": None,
        "industry": None,
        "description": organization.description,
    }


@router.get("/brand/facts")
def get_brand_facts(db: Session = Depends(get_db)):
    organization = get_demo_organization(db)

    facts = (
        db.query(BrandFact, BrandGuideline.title)
        .outerjoin(
            BrandGuideline,
            BrandFact.source_guideline_id == BrandGuideline.id
        )
        .filter(BrandFact.organization_id == organization.id)
        .order_by(BrandFact.fact_key.asc())
        .all()
    )

    return [
        {
            "id": str(fact.id),
            "key": fact.fact_key,
            "approved_value": fact.fact_value,
            "status": fact.status,
            "source_guideline": guideline_title,
        }
        for fact, guideline_title in facts
    ]


@router.get("/brand/terms")
def get_brand_terms(db: Session = Depends(get_db)):
    organization = get_demo_organization(db)

    terms = (
        db.query(BrandTerm)
        .filter(BrandTerm.organization_id == organization.id)
        .order_by(BrandTerm.term.asc())
        .all()
    )

    return [
        {
            "id": str(term.id),
            "term": term.term,
            "term_type": term.term_type,
            "approved_replacement": term.replacement,
            "explanation": term.explanation,
        }
        for term in terms
    ]