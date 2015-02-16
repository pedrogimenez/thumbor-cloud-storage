from setuptools import setup
from setuptools import find_packages

REQUIREMENTS = [
  "thumbor",
  "gcloud",
]

setup(
  name="thumbor_cloud_storage",
  version="1.0.0",
  author="Pedro Gimenez",
  author_email="me@pedro.bz",
  description="Thumbor's Google Cloud Storage loader",
  url="https://github.com/pedrogimenez/thumbor-cloud-storage",
  license="MIT",
  include_package_data=True,
  packages=find_packages(),
  install_requires=REQUIREMENTS,
  zip_safe=False
)
