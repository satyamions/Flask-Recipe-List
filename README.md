# Flask Recipe Maker

A web application built with Flask that allows users to add, edit, and delete recipes. The application supports image uploads for recipes and features a clean, responsive design.

## Features

- Add new recipes with ingredients, instructions, and an optional image.
- Edit existing recipes.
- Delete recipes with a confirmation prompt.
- Responsive design using Bootstrap 4.
- Image upload functionality.

## Requirements

To run this project, you'll need the following:

- Python 3.7 or higher
- Flask
- SQLAlchemy
- Flask-Migrate
- Jinja2
- Bootstrap 4
- AOS (Animate on Scroll) for animations

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/flask_recipe_maker.git
cd flask_recipe_maker
```

### Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Set up the database

```bash
flask --app main db init
flask --app main db migrate -m "Initial migration"
flask --app main db upgrade
```

## Configuration

You can configure the application settings in `config.py`. Ensure you have the correct settings for the following:

- `UPLOAD_FOLDER`: The directory where uploaded images will be stored.
- `SQLALCHEMY_DATABASE_URI`: The URI for your database.
- `SECRET_KEY`: A secret key for session management and CSRF protection.

## Running the Application

To start the application, use the following command:

```bash
flask --app main run
```

Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

## Project Structure

```
flask_recipe_maker/
│
├── main.py                # Main application file
├── config.py              # Configuration settings
├── models.py              # Database models
├── templates/             # HTML templates
│   ├── index.html
│   ├── add_recipe.html
│   └── edit_and_delete_recipe.html
├── static/                # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
├── migrations/            # Database migrations
└── README.md              # This README file
```

## Future Improvements

- Implement user authentication for personalized recipe management.
- Add pagination for the recipe list.
- Improve image handling with thumbnails and resizing.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The Python microframework used in this project.
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used for styling.
- [AOS](https://michalsnik.github.io/aos/) - For the scroll animations.
```

### Instructions to Include in the Project:

1. Place this `README.md` file** in the root of your project directory.
2. Add a `requirements.txt` file** with the dependencies needed to run the project:
   ```bash
   pip freeze > requirements.txt
   ```
