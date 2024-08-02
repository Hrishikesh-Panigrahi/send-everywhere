# Send Everywhere

Welcome to Send Everywhere, a Django project inspired by Send Anywhere. This project aims to provide a simple and efficient way to share files across devices seamlessly.

## Features

- **File Sharing**: Share files quickly without the need for accounts or complicated setups.
- **Sharing Methods**: Send Everywhere offers three options for sharing: key sharing (default), getting a link, and email, which are available after users log in.
- **User Authentication**: Users can access features of send everywhere after authenticating on the website.
- **Simple Interface**: Designed for easy navigation and use.

## Setup Instructions

1. **Clone the repository:**

```sh
git clone https://github.com/your-username/send-everywhere.git
cd send-everywhere
```

2. **Install dependencies:**

```sh
pip install -r requirements.txt
```

3. **Run migrations:**

```sh
python manage.py migrate
```

4. **Start the development server:**

```sh
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
- User Authentication: If you want to use additional features like getting a link for the file, or email, you need to log in to the website.

2. **Downloading Files:**

- Share the Files: After uploading, choose one of the following methods to share:
    - Key Sharing (default): Share the provided key with the recipient.
    - Get the Link: Generate a link to share with the recipient.
    - Email: Send the file directly to the recipient's email.
- The recipient can use the provided key or link, or check their email to access and download the file(s).

## Project Structure

The project contains a single Django app named `base`. The main URL pattern (`""`) directs to the `index` view in `views.py`, which handles file uploads and serves the home page.

## Technologies Used

- **Django**: Web framework for rapid development.
- **Python**: Programming language used for backend logic.
- **HTML/CSS**: Frontend styling and structure.

---

Enjoy using Send Everywhere for your file sharing needs! For any issues or feedback, please open an issue on GitHub.
