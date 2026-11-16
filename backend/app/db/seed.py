
from app.db.database import SessionLocal
from app.db.models import Organization, User, BrandFact, BrandTerm


def seed_database():
    db = SessionLocal()

    try:
        # Create demo organization
        organization = db.query(Organization).filter_by(
            name="TechNova"
        ).first()

        if not organization:
            organization = Organization(
                name="TechNova",
                description="Technology brand focused on smart devices."
            )
            db.add(organization)
            db.flush()

        # Create demo creator
        user = db.query(User).filter_by(
            email="creator@technova.demo"
        ).first()

        if not user:
            user = User(
                organization_id=organization.id,
                name="Demo Creator",
                email="creator@technova.demo",
                password_hash="DEMO_ONLY_NO_AUTH",
                role="CREATOR"
            )
            db.add(user)

        # Create demo manager
        manager = db.query(User).filter_by(
            email="manager@technova.demo"
        ).first()

        if not manager:
            manager = User(
                organization_id=organization.id,
                name="Demo Manager",
                email="manager@technova.demo",
                password_hash="DEMO_ONLY_NO_AUTH",
                role="MANAGER"
            )
            db.add(manager)


        # Approved brand facts
        facts = [
            ("battery_life", "24 hours"),
            ("price", "INR 1,499"),
        ]

        for key, value in facts:
            existing = db.query(BrandFact).filter_by(
                organization_id=organization.id,
                fact_key=key
            ).first()

            if not existing:
                db.add(BrandFact(
                    organization_id=organization.id,
                    fact_key=key,
                    fact_value=value,
                    status="APPROVED"
                ))

        # Brand terminology
        terms = [
            (
                "Smart Watch Professional",
                "PROHIBITED",
                "SmartWatch Pro",
                "Use the officially approved product name."
            ),
        ]

        for term, term_type, replacement, explanation in terms:
            existing = db.query(BrandTerm).filter_by(
                organization_id=organization.id,
                term=term
            ).first()

            if not existing:
                db.add(BrandTerm(
                    organization_id=organization.id,
                    term=term,
                    term_type=term_type,
                    replacement=replacement,
                    explanation=explanation
                ))

        db.commit()
        print("TechNova demo data seeded successfully!")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
