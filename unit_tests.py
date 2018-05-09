import unittest



def get_formatted_name(firstName, lastName):
	return (firstName + ' ' + lastName).title()


class GetFormattedNameTest(unittest.TestCase):
	"""Tests for get_formatted_name function"""
	expected = "Illia Rahavoi"

	def test_get_formatted_name(self):
		result = get_formatted_name("Illia", "Rahavoi")
		self.assertEqual(self.expected, result)

	def test_get_formatted_name_lower(self):
		result = get_formatted_name("illia", "rahavoi")
		self.assertEqual(self.expected, result)

	def test_get_formatted_name_upper(self):
		result = get_formatted_name("ILLIA", "RAHAVOI")
		self.assertEqual(self.expected, result)	


unittest.main()