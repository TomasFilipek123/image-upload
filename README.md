# Django REST API for Image Upload

This is a Django REST Framework API that allows users to upload images in PNG or JPG format. The API supports three built-in account tiers: Basic, Premium, and Enterprise. Users can upload their images and view their images. The API generates thumbnail links for users with different plans, and admin users can create arbitrary tiers and configure the thumbnail sizes, link to the originally uploaded file, and generate expiring links.
## Getting Started
### Prerequisites

   - Python 3.8 or higher
   - Django 3.2 or higher
   - Django REST Framework 3.12 or higher
   - Pillow 8.3 or higher
   

### Installation

1. Clone the repository:  
```console
https://github.com/TomasFilipek123/image-upload.git
```
2. Install the required packages:
```console
pip install -r requirements.txt
```
### Setting up the environment
1. Create a virtual environment (**env**):
```console
 py -m venv env
```
2. Activate virtual environment:
```console
env\Scripts\activate
```
3. Create migrations:
```console
py manage.py makemigrations
```
4. Run database migration:
```console
py manage.py migrate
```
5. Create a superuser:
```console
py manage.py createsuperuser
```
6. Start the server:
```console
py manage.py runserver
```
          
