def replace_contents_from_line(filename, new_content, starting_line_number):
  """Replaces the contents of a file with new content, starting from a specified line."""

  with open(filename, "r") as file:
    lines = file.readlines()

  lines[starting_line_number - 1:] = new_content.splitlines(keepends=True)  # Preserve line endings

  with open(filename, "w") as file:
    file.writelines(lines)

# Example usage:
new_content = """
# Read the contents of the README file
from pathlib import Path
this_directory = Path(__file__).parent.parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Autharmor",
    author="AuthArmor API Support",
    author_email="support@autharmor.com",
    url="https://autharmor.com",
    keywords=["Autharmor", "Authentication", "Authorization"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,  # noqa: E501
    package_data={"autharmor_python": ["py.typed"]},
)
"""
replace_contents_from_line("./sdk/setup.py", new_content, 26)
