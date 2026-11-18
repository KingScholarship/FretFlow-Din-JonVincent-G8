from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AccountFeatureTests(TestCase):
    def test_registration_creates_member_profile(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'guitarist',
            'first_name': 'Jon',
            'last_name': 'Vincent',
            'email': 'jon@example.com',
            'password1': 'Strong-pass-123',
            'password2': 'Strong-pass-123',
        })
        self.assertRedirects(response, reverse('accounts:dashboard'))
        user = User.objects.get(username='guitarist')
        self.assertEqual(user.role, User.Role.MEMBER)
        self.assertTrue(user.check_password('Strong-pass-123'))
        self.assertNotEqual(user.password, 'Strong-pass-123')

    def test_registration_rejects_duplicate_email_case_insensitively(self):
        User.objects.create_user(
            username='existing',
            email='jon@example.com',
            password='Strong-pass-123',
        )
        response = self.client.post(reverse('accounts:register'), {
            'username': 'another',
            'first_name': 'Jon',
            'last_name': 'Vincent',
            'email': 'JON@example.com',
            'password1': 'Strong-pass-123',
            'password2': 'Strong-pass-123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)

    def test_login_page_is_public(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_redirects_to_login(self):
        user = User.objects.create_user(username='member', password='Strong-pass-123')
        self.client.login(username='member', password='Strong-pass-123')

        response = self.client.post(reverse('accounts:logout'))

        self.assertRedirects(response, reverse('accounts:login'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={reverse('accounts:dashboard')}",
        )

    def test_member_cannot_open_admin_dashboard(self):
        user = User.objects.create_user(
            username='member',
            password='Strong-pass-123',
            role=User.Role.MEMBER,
        )
        self.client.login(username='member', password='Strong-pass-123')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertTemplateUsed(response, 'accounts/member_dashboard.html')

    def test_admin_role_uses_admin_dashboard(self):
        user = User.objects.create_user(
            username='admin',
            password='Strong-pass-123',
            role=User.Role.ADMIN,
        )
        self.client.login(username='admin', password='Strong-pass-123')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertTemplateUsed(response, 'accounts/admin_dashboard.html')

    def test_profile_updates_only_authenticated_user(self):
        user = User.objects.create_user(
            username='member',
            password='Strong-pass-123',
            email='old@example.com',
        )
        user.role = User.Role.MEMBER
        user.save(update_fields=('role',))
        self.client.login(username='member', password='Strong-pass-123')
        response = self.client.post(reverse('accounts:profile'), {
            'first_name': 'New',
            'last_name': 'Name',
            'email': 'new@example.com',
            'display_name': 'Jon V.',
            'contact_number': '09123456789',
        })
        self.assertRedirects(response, reverse('accounts:profile'))
        user.refresh_from_db()
        self.assertEqual(user.email, 'new@example.com')
        self.assertEqual(user.contact_number, '09123456789')
