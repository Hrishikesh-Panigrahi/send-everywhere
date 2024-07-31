# Send Everywhere

Welcome to Send Everywhere, a Django project inspired by Send Anywhere. This project aims to provide a simple and efficient way to share files across devices seamlessly.

## Features

- **File Sharing**: Share files quickly without the need for accounts or complicated setups.
- **Simple Interface**: Minimalist design for easy navigation and usage.
- **Security**: Uses Django's built-in security features to protect file transfers.

## Setup Instructions

1. **Clone the repository:**
```
git clone https://github.com/your-username/send-everywhere.git
cd send-everywhere
```

2. **Install dependencies:**
```
pip install -r requirements.txt
```

3. **Run migrations:**
```
python manage.py migrate
```

4. **Start the development server:**
```bash
python manage.py runserver
```

5. **Access the application:**
Open your web browser and go to `http://localhost:8000/` to use Send Everywhere.

## Docker Setup Instructions

Alternatively, you can run Send Everywhere using Docker for easy deployment:

1. **Pull Docker Image:**
```bash
docker pull hrishikeshpanigrahi025/send-everywhere
```

2. **Run Docker Container:**
```bash
docker run -d -p 8000:8000 hrishikeshpanigrahi025/send-everywhere
```

3. **Check Docker Container Status:**
```bash
docker ps
```

4. **Access Container Files (Optional):**
```bash
docker exec -it <container_name> sh
```
- Use this command to explore files or debug inside the running container.

5. **Access the application:**
Open your web browser and go to `http://localhost:8000/` to use Send Everywhere.

## Usage

1. **Uploading Files:**
- Navigate to the home page.
- Click on the upload button and select the file(s) you want to share.

2. **Downloading Files:**
- Share the provided link with the recipient.
- Recipient can access the link and download the file(s).

## Project Structure

The project contains a single Django app named `base`. The main URL pattern (`""`) directs to the `index` view in `views.py`, which handles file uploads and serves the home page.

## Technologies Used

- **Django**: Web framework for rapid development.
- **Python**: Programming language used for backend logic.
- **HTML/CSS**: Frontend styling and structure.


---

Enjoy using Send Everywhere for your file sharing needs! For any issues or feedback, please open an issue on GitHub.
