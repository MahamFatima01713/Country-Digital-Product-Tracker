from datetime import date

from database import Base, SessionLocal, engine
from models import Project

# Real UNDP project data, from UNDP's open data portal (open.undp.org),
# name, country, next_milestone and milestone_date are UNDP's own data:
# next_milestone is the project's first listed output, milestone_date is
# the project's end date. status is derived from the end date: an end date
# in the future means Ongoing, a past end date means Completed. owner is
# the UNDP country office, because UNDP publishes no single person as owner.
SAMPLE_PROJECTS = [
    {
        "name": "Regional Centre of Competence For Digital And Artificial Intelligence Skilling in Kenya",
        "country": "kenya",
        "owner": "UNDP Kenya",
        "topic": "AI",
        "status": "Ongoing",
        "next_milestone": "Regional Centre of Competence For Digital And Artificial Intelligence Skilling in Kenya",
        "milestone_date": date(2026, 12, 31),
        "status_note": "The Regional Centre of Competence for Digital and AI Skilling is a flagship initiative led by the Government of Kenya in collaboration with UNDP and key partners, hosted at the Kenya School of Government.",
    },
    {
        "name": "Artificial Intelligence Institute",
        "country": "Serbia",
        "owner": "UNDP Serbia",
        "topic": "AI",
        "status": "Ongoing",
        "next_milestone": "AI Inst.&Legal framework",
        "milestone_date": date(2026, 12, 31),
        "status_note": "Harnessing AI for the common good - facilitating an AI-friendly ecosystem in Serbia",
    },
    {
        "name": "Artificial Intelligence and Digital Public Infrastructure for Sustainable Development",
        "country": "Global",
        "owner": "UNDP Global Programme",
        "topic": "AI",
        "status": "Completed",
        "next_milestone": "Artificial Intelligence and Digital Public Infrastructure for Sustainable Development",
        "milestone_date": date(2026, 9, 30),
        "status_note": "Artificial Intelligence and Digital Public Infrastructure for Sustainable Development",
    },
    {
        "name": "Digital Solutions for Recovery (PIP)",
        "country": "Afghanistan",
        "owner": "UNDP Afghanistan",
        "topic": "Digital",
        "status": "Completed",
        "next_milestone": "Digital Solutions for Recovery (PIP)",
        "milestone_date": date(2026, 10, 11),
        "status_note": "Digital Solutions for Recovery (PIP) Project is implementing by the United Nation Development Programme UNDP Country Office for Afghanistan.",
    },
    {
        "name": "Digital Transformation Program",
        "country": "Belize",
        "owner": "UNDP Belize",
        "topic": "Digital",
        "status": "Ongoing",
        "next_milestone": "Digital Transformation Program",
        "milestone_date": date(2026, 12, 31),
        "status_note": 'The "Digital Inclusion" proposal seeks to facilitate access, adoption, and application of information and communication technologies by marginalized communities as a means for socio-economic prosperity.',
    },
    {
        "name": "Digital transformation in Public sector",
        "country": "Bosnia and Herzegovina",
        "owner": "UNDP Bosnia and Herzegovina",
        "topic": "Digital",
        "status": "Ongoing",
        "next_milestone": "Digital transformation",
        "milestone_date": date(2026, 11, 30),
        "status_note": "Digital transformation in the public sector in Bosnia and Herzegovina - create better pre-conditions for accelerated digital transformation in the public sector.",
    },
    {
        "name": "Green and Digital Innovation Cooperation Project (GDIP)",
        "country": "China",
        "owner": "UNDP China",
        "topic": "Digital",
        "status": "Ongoing",
        "next_milestone": "Green and Digital Innovation Cooperation Project (GDIP)",
        "milestone_date": date(2028, 12, 31),
        "status_note": 'This project supports the construction of Hainan Province\'s "Zero-Carbon Island" and "Free Trade Port" initiatives while contributing to the sustainable development of the China-EU (Baoting) Green and Digital Innovation Zone.',
    },
    {
        "name": "Supporting Gender-Responsive Transparency and Data Privacy in Albania's Judiciary",
        "country": "Albania",
        "owner": "UNDP Albania",
        "topic": "Data",
        "status": "Ongoing",
        "next_milestone": "Supporting Gender-Responsive Transparency and Data Privacy in Albania's Judiciary",
        "milestone_date": date(2027, 12, 31),
        "status_note": "The project aims to strengthen the Supreme Court of Albania's capacity to balance transparency and privacy in the publication of judicial decisions.",
    },
    {
        "name": "Data for Food Security Preparedness",
        "country": "Djibouti",
        "owner": "UNDP Djibouti",
        "topic": "Data",
        "status": "Completed",
        "next_milestone": "Data for Food Security",
        "milestone_date": date(2025, 7, 30),
        "status_note": "Data Collection and Survey to develop National Solidarity Pact for Food Security Preparedness",
    },
    {
        "name": "Localizing Data Science for Climate Change Adaptation",
        "country": "India",
        "owner": "UNDP India",
        "topic": "Data",
        "status": "Ongoing",
        "next_milestone": "Localizing Data Science for Climate Change Adaptation",
        "milestone_date": date(2026, 12, 31),
        "status_note": "This is the preparatory phase of the project on creating models of resilience in agriculture through integration of climate data science and local knowledge base on agriculture in four different agroclimatic zones in India.",
    },
]


def seed_projects():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if db.query(Project).count() > 0:
            print("Projects table already has data. Skipping seeding.")
            return

        for project_data in SAMPLE_PROJECTS:
            db.add(Project(**project_data))

        db.commit()
        print("Added 10 sample projects.")
    finally:
        db.close()


if __name__ == "__main__":
    seed_projects()
