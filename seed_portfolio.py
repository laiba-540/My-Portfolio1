import os
import django

# Set up django environment context
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def seed_data():
    print("=========================================================")
    print("Seeding database with Laiba Tanseer's portfolio data...")
    print("=========================================================")
    
    # 1. Clear existing data to avoid duplicates
    Bio.objects.all().delete()
    Education.objects.all().delete()
    Skill.objects.all().delete()
    Experience.objects.all().delete()
    Project.objects.all().delete()
    
    # 2. Seed Biography (Bio)
    Bio.objects.create(
        name="Laiba Tanseer",
        title="Computer Science Undergraduate",
        summary=(
            "Passionate Computer Science student at the University of Management and Technology (UMT) "
            "with a strong interest in Artificial Intelligence, Backend Development, and Problem Solving. "
            "I enjoy building intelligent and scalable software solutions using modern technologies and "
            "continuously improving my programming skills through practical projects."
        ),
        email="laibtanser@gmail.com",
        linkedin="laiba-tanseer",
        typing_roles="Computer Science Student, AI Enthusiast, Backend Developer, Problem Solver"
    )
    print("[OK] Biography record seeded.")

    # 3. Seed Education
    Education.objects.create(
        institution="University of Management and Technology (UMT)",
        degree="Bachelor of Computer Science",
        status="Undergraduate",
        start_year=2022,
        description="Currently pursuing Bachelor of Computer Science degree with focus on Software Engineering, Artificial Intelligence, and Database Systems. Actively engaged in development projects and problem solving."
    )
    print("[OK] Education record seeded.")

    # 4. Seed Skills
    skills_data = [
        # Languages & Frameworks
        {"name": "Python", "proficiency": 90, "category": "Languages & Frameworks", "order": 1},
        {"name": "Django", "proficiency": 85, "category": "Languages & Frameworks", "order": 2},
        {"name": "FastAPI", "proficiency": 80, "category": "Languages & Frameworks", "order": 3},
        
        # AI & Prompt Engineering
        {"name": "Artificial Intelligence", "proficiency": 75, "category": "AI & Advanced Tech", "order": 4},
        {"name": "Prompt Engineering", "proficiency": 85, "category": "AI & Advanced Tech", "order": 5},
        
        # CS Core & Databases
        {"name": "Object-Oriented Programming (OOP)", "proficiency": 85, "category": "Core Engineering", "order": 6},
        {"name": "Database Management", "proficiency": 80, "category": "Core Engineering", "order": 7},
        {"name": "Problem Solving", "proficiency": 90, "category": "Core Engineering", "order": 8},
    ]
    for skill in skills_data:
        Skill.objects.create(**skill)
    print(f"[OK] {len(skills_data)} skills records seeded.")

    # 5. Seed Experience
    Experience.objects.create(
        title="Personal Projects Experience",
        description=(
            "Developed multiple academic and personal software solutions using Python, Django, FastAPI, "
            "Artificial Intelligence, and database technologies. Gained practical experience through project-based "
            "learning, focusing on backend development, AI applications, database management, and software "
            "engineering best practices.\n\n"
            "Key learnings and focus areas:\n"
            "- Database Schema design & Integration: Designed robust database schemas using Django ORM and SQLite.\n"
            "- AI pipeline implementations: Integrated machine learning algorithms and deep learning models into Python backends.\n"
            "- API design & routing: Managed backend architectures using FastAPI.\n"
            "- Responsive frontend development: Created fluid mobile-first layouts utilizing Bootstrap 5 and modern CSS features."
        )
    )
    print("[OK] Experience record seeded.")

    # 6. Seed Projects
    projects_data = [
        {
            "title": "Pneumonia Detection System",
            "description": "AI-powered medical image classification system that detects pneumonia from chest X-ray images using deep learning techniques.",
            "technologies": "Python, Deep Learning, Artificial Intelligence",
            "github_link": "https://github.com/laiba-tanseer",
            "order": 1
        },
        {
            "title": "Hospital Management System",
            "description": "A complete hospital management application for managing patients, doctors, appointments, medical records, and hospital operations.",
            "technologies": "Django, Python, SQLite",
            "github_link": "https://github.com/laiba-tanseer",
            "order": 2
        },
        {
            "title": "To-Do List Application",
            "description": "A task management web application that allows users to create, edit, complete, and delete daily tasks.",
            "technologies": "Django, HTML, CSS, JavaScript",
            "github_link": "https://github.com/laiba-tanseer",
            "order": 3
        },
        {
            "title": "Crop Recommender System",
            "description": "A machine learning application that recommends the most suitable crop based on soil nutrients and environmental conditions.",
            "technologies": "Python, Machine Learning, Artificial Intelligence",
            "github_link": "https://github.com/laiba-tanseer",
            "order": 4
        }
    ]
    for project in projects_data:
        Project.objects.create(**project)
    print(f"[OK] {len(projects_data)} projects records seeded.")
    
    print("=========================================================")
    print("Database seeding completed successfully!")
    print("=========================================================")

if __name__ == '__main__':
    seed_data()
