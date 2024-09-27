# Ticket Management System

This is a Django-based Ticket Management System that allows users to create, update, view, and manage tickets. The system includes features for superusers, staff, and normal users to handle ticketing efficiently. It also supports comments, and user performance tracking.

## Features

- **Ticket Management**: Users can create, update, and delete tickets. Tickets can be marked as resolved or unresolved.
- **Search Functionality**: Users and staff can search for tickets based on title, customer name, or issue description.
- **Comments**: Users can add comments to tickets, and all comments are displayed in the ticket detail view.
- **Urgent Tickets**: Filter and view urgent tickets.
- **User Performance Tracking**: Track the number of tickets resolved by each user with user performance views and charts.
## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Activate env:
    ```bash
     myenv3/scripts/activate
    ```
4. Apply migrations:
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- **Superusers**: Can view all tickets, manage urgent tickets, mark tickets as resolved/unresolved, and view staff performance.
- **Staff**: Can view tickets assigned to them, filter based on urgency, and resolve or comment on tickets.
- **Normal Users**: Can create tickets and view the status of tickets they have created.

### Views Overview

- **TicketListView**: Lists all tickets for superusers, staff, or normal users.
- **TicketDetailView**: Displays the details of a ticket, including comments.
- **TicketCreateView**: Allows users to create new tickets.
- **TicketUpdateView**: Allows users or staff to update ticket details.
- **TicketDeleteView**: Allows deletion of a ticket (superusers only).
- **SearchResultView**: Allows users to search for tickets based on keywords.
- **UserPerformanceListView**: Shows a list of users with the number of tickets resolved.
- **UserPerformanceDetailView**: Shows detailed performance stats for an individual user.




