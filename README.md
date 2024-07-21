
# BookMyTable - PP4

**BookMyTable** is a web application designed to streamline the restaurant reservation process and menu management. This project, developed by [Florin Pinta (xttrust)](https://github.com/xttrust), serves as a comprehensive solution for both diners and restaurant staff, offering an intuitive platform to handle reservations and menu items efficiently.

Explore the live application at [BookMyTable Deployed Site](https://bookmytable-8de20a7bca65.herokuapp.com/).

![BookMyTable Image](./docs/images/banner-image.png)

## User Experience

### User Stories

#### New User

1. As a user, I can **register for an account** so that I can make and manage reservations. [#6](https://github.com/xttrust/BookMyTable/issues/6)
2. As a user, I can **log into my account** so that I can access my reservations and profile. [#7](https://github.com/xttrust/BookMyTable/issues/7)
3. As a user, I can **view available tables for a specific date and time** so that I can choose a suitable table for my reservation. [#9](https://github.com/xttrust/BookMyTable/issues/9)
4. As a user, I can **book a table** so that I can dine at the restaurant. [#11](https://github.com/xttrust/BookMyTable/issues/11)
5. As a user, I can **view my upcoming reservations** so that I can manage my bookings. [#12](https://github.com/xttrust/BookMyTable/issues/12)
6. As a user, I can **see a booking confirmation on the website** so that I have proof of my reservation. [#17](https://github.com/xttrust/BookMyTable/issues/17)

#### Existing User

1. As an existing user, I can **view and manage my reservations** so that I can keep track of my dining plans. [#12](https://github.com/xttrust/BookMyTable/issues/12)

#### Admin

1. As an admin, I can **view and manage all bookings** so that I can ensure smooth operations and resolve any issues promptly. [#14](https://github.com/xttrust/BookMyTable/issues/14)
2. As an admin, I can **manage menu items** so that I can update and maintain the restaurant’s offerings. [#23](https://github.com/xttrust/BookMyTable/issues/23)
3. As an admin, I can **manage menu categories** so that I can organize the restaurant’s menu effectively. [#22](https://github.com/xttrust/BookMyTable/issues/22)
5. As an admin, I can **display formatted descriptions in the admin list view** so that information is presented clearly. [#24](https://github.com/xttrust/BookMyTable/issues/24)

#### Testing and Documentation

1. As a developer, I can **write tests** to ensure the application functions as expected. [#20](https://github.com/xttrust/BookMyTable/issues/20)
2. As a developer, I can **write documentation** so that users and developers understand how to use and contribute to the project. [#21](https://github.com/xttrust/BookMyTable/issues/21)

### Site Goals

1. **Simplify the Restaurant Reservation Process**: Provide an intuitive and efficient platform for users to book and manage restaurant reservations effortlessly.
   
2. **Enhance Dining Experience**: Offer users the ability to view detailed information about available tables, including real-time availability, to ensure a seamless dining experience.
   
3. **Streamline Menu Management**: Allow restaurant staff to easily update and manage menu items and categories, ensuring that diners have access to the latest offerings.
   
4. **Facilitate User Account Management**: Enable users to create, access, and manage their accounts, reservations, and preferences securely and conveniently.
   
5. **Improve Administrative Efficiency**: Equip restaurant administrators with robust tools to oversee reservations, manage menu items, and handle customer interactions efficiently.
   
6. **Ensure Scalability and Performance**: Develop a scalable platform that can handle varying levels of traffic and user activity without compromising performance.

## Scope

The **BookMyTable** application aims to provide a streamlined and efficient platform for restaurant reservations and menu management. The scope of the project includes:

1. **User Account Management**: Enabling users to register, log in, and manage their profiles.
2. **Table Reservation System**: Allowing users to view available tables, make reservations, and manage their bookings.
3. **Menu Management**: Facilitating restaurant staff in managing menu items and categories.
4. **Administrative Features**: Offering tools for administrators to oversee reservations, manage users, and maintain restaurant details.
5. **System Notifications**: Providing clear notifications for user actions such as login, logout, registration, table reservations, and updates to ensure a smooth user experience.
6. **Testing and Documentation**: Ensuring comprehensive testing and providing clear documentation for developers and users.

## Epics

<details>
<summary>Epic 1: User Account Management</summary>

- **User Registration**: As a user, I want to register for an account to manage reservations. [#6](https://github.com/xttrust/BookMyTable/issues/6)
- **User Login**: As a user, I want to log into my account to access my reservations. [#7](https://github.com/xttrust/BookMyTable/issues/7)

</details>

<details>
<summary>Epic 2: Table Reservation</summary>

- **View Available Tables**: As a user, I want to view available tables for a specific date and time. [#9](https://github.com/xttrust/BookMyTable/issues/9)
- **Make a Reservation**: As a user, I want to book a table for dining. [#11](https://github.com/xttrust/BookMyTable/issues/11)
- **View My Reservations**: As a user, I want to view and manage my upcoming reservations. [#12](https://github.com/xttrust/BookMyTable/issues/12)

</details>

<details>
<summary>Epic 3: Admin Management</summary>

- **Manage Reservations**: As an admin, I want to view and manage all bookings. [#14](https://github.com/xttrust/BookMyTable/issues/14)
- **Manage Menu Items**: As an admin, I want to manage menu items. [#23](https://github.com/xttrust/BookMyTable/issues/23)
- **Manage Menu Categories**: As an admin, I want to manage menu categories. [#22](https://github.com/xttrust/BookMyTable/issues/22)
- **Display Formatted Descriptions in Admin List View**: As an admin, I want formatted descriptions in the admin list view. [#24](https://github.com/xttrust/BookMyTable/issues/24)

</details>

<details>
<summary>Epic 4: System Notifications</summary>

- **Login Notification**: As a user, I want to receive a notification upon successful login.
- **Logout Notification**: As a user, I want to receive a notification upon successful logout.
- **Registration Notification**: As a user, I want to receive a notification upon successful registration.
- **Reservation Notification**: As a user, I want to receive a notification upon successful table reservation.
- **Update Reservation Notification**: As a user, I want to receive a notification when a reservation is updated.
- **Delete Reservation Notification**: As a user, I want to receive a notification when a reservation is deleted.

</details>

<details>
<summary>Epic 5: Testing and Documentation</summary>

- **Write Tests**: As a developer, I want to write tests to ensure the application functions correctly. [#20](https://github.com/xttrust/BookMyTable/issues/20)
- **Write Documentation**: As a developer, I want to write documentation to help users and future developers. [#21](https://github.com/xttrust/BookMyTable/issues/21)

</details>



## Design

### Goal

The design of **BookMyTable** aims to provide a clean, modern, and user-friendly interface that enhances the user experience for both diners and restaurant staff. By utilizing the default Bootstrap 5 theme, we ensure a responsive and consistent look across different devices and screen sizes. This choice simplifies the design process while maintaining a professional appearance.

### Colour Scheme

The default Bootstrap 5 color scheme has been selected for **BookMyTable**. These colors are carefully chosen to provide a balanced and visually appealing aesthetic that suits a wide range of applications. The Bootstrap 5 palette ensures excellent readability and accessibility, which is essential for a diverse user base. The familiar and neutral tones help create a welcoming and easy-to-navigate environment for users.

### Database Diagram

![Database Diagram](./docs/images/database-diagram.png)

