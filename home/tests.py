from django.test import TestCase, Client
from django.urls import reverse
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project
from contact.models import ContactMessage

class PortfolioTests(TestCase):

    def setUp(self):
        # Create test instances of models
        self.bio = Bio.objects.create(
            name="Laiba Tanseer",
            title="Computer Science Undergraduate",
            summary="Passionate CS student at UMT.",
            email="laibtanser@gmail.com",
            linkedin="laiba-tanseer",
            typing_roles="Developer, AI Enthusiast"
        )
        
        self.edu = Education.objects.create(
            institution="UMT",
            degree="Bachelor of Computer Science",
            status="Undergraduate",
            start_year=2022
        )
        
        self.skill = Skill.objects.create(
            name="Python",
            proficiency=90,
            category="Technical"
        )
        
        self.experience = Experience.objects.create(
            title="Personal Projects Experience",
            description="Built some awesome projects."
        )
        
        self.project = Project.objects.create(
            title="Hospital Management System",
            description="Manage hospital logs.",
            technologies="Django, SQLite, Python",
            order=1
        )
        
        self.client = Client()

    def test_home_view_status_code_and_content(self):
        # Verify landing page returns 200 and loads context
        url = reverse('home:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Check that context variables exist and are populated
        self.assertEqual(response.context['bio'].name, "Laiba Tanseer")
        self.assertEqual(len(response.context['education_list']), 1)
        self.assertEqual(len(response.context['skills_list']), 1)
        self.assertEqual(response.context['experience'].title, "Personal Projects Experience")
        self.assertEqual(len(response.context['project_list']), 1)
        
        # Verify page contents contain dynamic info
        self.assertContains(response, "Laiba Tanseer")
        self.assertContains(response, "University of Management and Technology")
        self.assertContains(response, "Hospital Management System")

    def test_contact_form_submission_ajax_success(self):
        # Test contact form AJAX submission
        url = reverse('contact:contact_submit')
        post_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Inquiry',
            'message': 'Hello, this is a test message.'
        }
        # Simulate AJAX request
        response = self.client.post(
            url, 
            post_data, 
            headers={'x-requested-with': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        
        # Verify it was saved to the database
        messages = ContactMessage.objects.filter(email='test@example.com')
        self.assertEqual(messages.count(), 1)
        self.assertEqual(messages.first().full_name, 'Test User')

    def test_contact_form_submission_validation_error(self):
        # Test validation failure (missing message)
        url = reverse('contact:contact_submit')
        post_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Inquiry',
            'message': ''  # empty
        }
        response = self.client.post(
            url, 
            post_data, 
            headers={'x-requested-with': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        
        # Ensure nothing was saved
        messages = ContactMessage.objects.filter(email='test@example.com')
        self.assertEqual(messages.count(), 0)

    def test_individual_app_json_endpoints(self):
        # Test bio JSON endpoint
        bio_url = reverse('bio:bio_detail')
        response = self.client.get(bio_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Laiba Tanseer")

        # Test skills JSON endpoint
        skills_url = reverse('skills:skills_list')
        response = self.client.get(skills_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['name'], "Python")

        # Test projects JSON endpoint
        projects_url = reverse('projects:project_list')
        response = self.client.get(projects_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['title'], "Hospital Management System")
