from django.test import TestCase
from django.urls import reverse

from portfolio.models import About, Project


class ProjectModelTests(TestCase):
	def test_project_str_returns_title(self):
		project = Project.objects.create(
			title="NeuralPet",
			github_link="https://github.com/example/neuralpet",
			description="AI virtual pet.",
		)

		self.assertEqual(str(project), "NeuralPet")


class AboutModelTests(TestCase):
	def test_about_str_is_static_label(self):
		about = About.objects.create(
			resume_link="https://example.com/resume.pdf",
			paragraph1="First paragraph",
			paragraph2="Second paragraph",
		)

		self.assertEqual(str(about), "About Content")


class ProjectsPageTests(TestCase):
	def test_projects_page_returns_200(self):
		response = self.client.get(reverse("projects"))

		self.assertEqual(response.status_code, 200)

	def test_projects_page_uses_correct_template(self):
		response = self.client.get(reverse("projects"))

		self.assertTemplateUsed(response, "portfolio/projects.html")

	def test_projects_page_displays_project_content(self):
		Project.objects.create(
			title="Weapon Forge",
			github_link="https://github.com/example/weapon-forge",
			live_link="https://example.com/weapon-forge",
			description="Procedural weapon generation game.",
		)

		response = self.client.get(reverse("projects"))

		self.assertContains(response, "Weapon Forge")
		self.assertContains(response, "https://github.com/example/weapon-forge")
		self.assertContains(response, "https://example.com/weapon-forge")
		self.assertContains(response, "Procedural weapon generation game.")


class AboutPageTests(TestCase):
	def test_about_page_returns_200(self):
		response = self.client.get(reverse("about"))

		self.assertEqual(response.status_code, 200)

	def test_about_page_uses_correct_template(self):
		response = self.client.get(reverse("about"))

		self.assertTemplateUsed(response, "portfolio/about.html")

	def test_about_page_displays_about_content(self):
		About.objects.create(
			resume_link="https://example.com/resume.pdf",
			paragraph1="I build modular software systems.",
			paragraph2="I also enjoy game design and outdoor activities.",
		)

		response = self.client.get(reverse("about"))

		self.assertContains(response, "https://example.com/resume.pdf")
		self.assertContains(response, "I build modular software systems.")
		self.assertContains(
			response,
			"I also enjoy game design and outdoor activities.",
		)

	def test_about_page_uses_default_resume_link_when_blank(self):
		About.objects.create(
			resume_link="",
			paragraph1="Paragraph one",
			paragraph2="",
		)

		response = self.client.get(reverse("about"))

		self.assertContains(response, '/static/files/resume.pdf')
