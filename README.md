# "Quotes" Website Project

## Project Overview

This repository hosts a Python-based Django project titled "Quotes", a dynamic website dedicated to the exploration and sharing of famous quotations. 
The site serves as an educational platform to demonstrate practical applications of Django, highlighting advanced features like user authentication and database migrations. 
The project aims to provide a practical demonstration of advanced Django features, database handling, and personalized user management.

## Key Features

- **Viewing Content:** Visitors can view all uploaded quotes and read detailed biographies of authors without logging in.
- **User Authentication:** Supports user registration and login, enabling personalized experiences on the site.
- **User Profile Management:** Users can set and update their profile pictures (avatars), personalizing their interaction with the site.
- **Author and Quote Management:** Registered users have the privilege to add, edit and delete authors, tags, and quotes. This makes the site interactive and continuously evolving.
- **Tagging System:** Registered users can create tags for quotes, facilitating efficient categorization and retrieval, and enhancing the browsing experience.
- **Data Migration:** Demonstrates robust data migration from Atlas MongoDB to PostgreSQL, showcasing the handling of data across different database systems.
- **Search Functionality:** Features a tag-based search that allows visitors to find all quotes associated with a selected tag.
- **Top Ten Tags:** Displays the ten most popular tags dynamically, highlighting the most talked-about topics.
- **Pagination:** Implements pagination to manage the display of quotes efficiently, equipped with `next` and `previous` navigation buttons for ease of access.

## Technologies Used

- **Django:** Used for the backend framework, facilitating rapid development and clean, pragmatic design.
- **PostgreSQL:** Acts as the primary relational database management system for robust data handling.
- **Poetry:** Manages dependencies and packages, ensuring a consistent and reproducible virtual development environment.
- **Docker Compose:** Simplifies deployment by using containerization to manage service configurations.

## Installation and Usage

### Setting Up the Project

- **Clone the Repository:**
```bash
git clone https://github.com/alex-nuclearboy/goit-python-web-hw10.git
```

- **Navigate to the Project Directory:**
```bash
cd goit-python-web-hw10
```

- **Activate the Poetry Environment and Install Dependencies:**
```bash
poetry shell
poetry install --no-root
```

- **Start the PostgreSQL Server:**
```bash
docker compose up -d
```

### Database Migration and Data Transfer

- **Navigate to the Django project Directory:**
```bash
cd quotes_project/
```

- **Create Tables in the Database:**
    - Unix/Linux/macOS:
    ```bash
    python3 manage.py migrate
    ```
    - Windows:
    ```powershell
    py manage.py migrate
    ```

- **Migrate Data from Atlas MongoDB:**
    - Unix/Linux/macOS:
    ```bash
    python3 -m utils.migration
    ```
    - Windows:
    ```powershell
    py -m utils.migration
    ```

### Starting the Server

- Once the migrations and data transfer are complete, you can start the Django development server:
    - Unix/Linux/macOS:
    ```bash
    python3 manage.py runserver
    ```
    - Windows:
    ```powershell
    py manage.py runserver
    ```

### Accessing the Application

After starting the server, open a web browser and visit the following URL to access the "Quotes" application:

[http://127.0.0.1:8000/quotesapp/](http://127.0.0.1:8000/quotesapp/)

## How to Use the "Quotes" Website

Once you have the "Quotes" website running, here's how you can explore and interact with the site:

### Viewing Quotes and Authors

- **Browse Quotes:** Upon visiting the main page at [http://127.0.0.1:8000/quotesapp/](http://127.0.0.1:8000/quotesapp/), you'll be greeted with a list of all the quotes uploaded to the site. Each quote is displayed with its content, the author's name, and associated tags.
- **Learn About Authors:** Each author's name is a clickable link. Clicking on an author's name will take you to a dedicated page that includes a biography of the author.

### Interacting with the Site as a Registered User

After registering and logging in, you gain additional capabilities:

- **Add New Quotes, Authors, and Tags:** Authenticated users can contribute to the site by adding new quotes and the authors who said them. You can also create tags to help categorize quotes, making them easier to find through search or tag-based navigation.
- **Edit and Delete Entries:** If you have added a quote, an author, or a tag, you can also edit or remove these entries. This helps in keeping the information up to date and accurate.
- **Update Your Profile:** Users can update their personal information and profile picture (avatar) from the profile page. This feature allows users to express their personality and preferences.

### Using the Search Functionality

- **Search by Tags:** The site includes a tag-based search feature, where clicking on a tag from the "Top Ten Tags" section or any tag listed under a quote will display all quotes associated with that tag. This is useful for users interested in specific themes or subjects.

### Navigation and Accessibility

- **Pagination Controls:** While browsing quotes, you can use the pagination controls at the bottom of the page to navigate between pages of quotes. This makes it easy to browse through large numbers of entries without overwhelming the user.


## Stopping the Server and Exiting

When you are finished using the "Quotes" website, follow these steps to properly shut down the server and exit the development environment:

- **Stopping the Server**

To stop the Django development server, you simply need to press `CTRL+C` in the terminal window where the server is running. This will terminate the server process.

- **Shutting Down the PostgreSQL Server**

If you've started the PostgreSQL server using Docker Compose and wish to stop it, you can use the following command:

```bash
docker compose down
```

This command stops the running containers and removes the containers created by `docker compose up`, along with their networks. It’s a clean way to ensure that no unnecessary Docker processes remain running.
If you wish to stop the container but not remove it, you can use:
```bash
docker compose stop
```

- **Exiting the Poetry Environment**
```bash
exit
```

This command will deactivate the virtual environment and return you to your system's default environment.
