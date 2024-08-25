# FastFoodHub 🍔🍟

Welcome to **FastFoodHub**! 🚀 Your go-to place for delicious, fast, and convenient food delivery. This project combines a Django backend with a responsive and aesthetically pleasing front-end using HTML, CSS, Tailwind CSS, Bootstrap, and JavaScript.

## Features 🌟

- **Dynamic Menu**: Explore a diverse menu with categories and detailed item descriptions. 🍕🍔
- **Real-Time Order Tracking**: Stay updated with real-time tracking of your orders. 📦
- **Special Deals**: Discover and grab the latest offers and promotions. 🎉
- **Beautiful UI:**: Experience a visually appealing and user-friendly interface with smooth animations. ✨
## Tech Stack 🛠️

- **Frontend**: HTML, CSS, Tailwind CSS, Bootstrap, JavaScript
- **Backend**: Django
- **Database**: PostgreSQL (or SQLite for development)
- **Static Files**: Served through Django

### Setup 🔧

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/FastFoodHub.git
   cd FastFoodHub

2. **Set Up the Backend 🐍**
   - Create a virtual environment: 

      ```bash
      python -m venv .venv
   - Activate the virtual environment:
   
      ```bash
      source .venv/bin/activate
   - Install dependencies:

      ```bash
      pip install -r requirements.txt

   - Apply migrations:
   
      ```bash
      python manage.py migrate
     
   - Create a superuser:
   
      ```bash
      python manage.py createsuperuser


   - Run the server:
   
      ```bash
      python manage.py runserver

3. **Set Up the Frontend ⚛️**
   - Navigate to the `frontend` directory:
   
      ```bash
      cd frontend

   - Install dependencies:
   
      ```bash
      npm install

   - Build the React app:
   
      ```bash
      npm run build
4. **Link Frontend with Django 🔗**
   Copy the React build files to Django's static directory:
   
    ```bash
   cp -r build/* ../fastfood_app/static/

5. **Access the Application 🌐**
Open your browser and go to http://127.0.0.1:8000 to see FastFoodHub in action! 🍴

## Contributing 🤝

We welcome contributions to enhance the FastFoodHub project. Please follow these steps to contribute:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Commit your changes with clear messages.
* Push to your forked repository.
* Create a pull request.

## License 📜

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📬

For any questions or feedback, feel free to reach out:

* GitHub: SulemanAwais
