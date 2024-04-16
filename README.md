# SPEC-1: Mach-Suri

## Background

The development of this web application is driven by the need to provide a dedicated platform where contract workers can share and access job leads. This serves to facilitate a community-driven approach to job discovery, catering specifically to the needs of contract workers who often rely on sporadic and varied job opportunities. By enabling a central hub for sharing and accessing job leads, the platform aims to enhance the visibility of available work and improve the job acquisition process for contract workers. The primary users of this application are contract workers looking for an efficient way to access and share job opportunities.

## Requirements

### Functional Requirements

**Must Have:**
- User registration system to allow contract workers to create and manage their profiles.
- Posting job leads functionality enabling users to share new job opportunities.
- Basic job search functionality to allow users to find job leads posted by others.

**Should Have:**
- Advanced filtering options in job searches, including location, job title, skills required, and compensation range.
- Displaying job postings with summary information on the main search page, with the option to click on a posting for detailed information.

### Non-Functional Requirements

- The application should be scalable to support an increase in user base and job postings without performance degradation.
- Response times for user interactions should be consistently under 2 seconds.
- The platform must ensure robust security measures for user data protection, especially concerning personal and payment information.

## Method

### Architecture Overview

The application will be developed using a monolithic architecture model, leveraging the Django web framework. This approach simplifies the development and deployment processes and is ideal for applications expected to scale moderately. Django's robustness and built-in features will facilitate rapid development and secure handling of user data.

### Database Schema

Using a relational SQL database, the initial schema will include tables for Users and JobPostings:

**Users Table:**

| Column           | Description                                   |
|------------------|-----------------------------------------------|
| `userId`         | Primary key, uniquely identifies a user.      |
| `username`       | User's chosen username.                       |
| `email`          | User's email address.                         |
| `passwordHash`   | Hash of the user's password for secure storage. |
| `registrationDate` | Date and time the user registered on the platform. |

**JobPostings Table:**

| Column             | Description                                   |
|--------------------|-----------------------------------------------|
| `jobId`            | Primary key, uniquely identifies a job posting. |
| `posterId`         | Foreign key, references the userId from the Users table. |
| `title`            | Title of the job posting.                     |
| `description`      | Detailed description of the job.              |
| `skillsRequired`   | List of required skills for the job.          |
| `location`         | Location of the job.                          |
| `compensationRange` | Compensation range offered for the job.      |
| `postingDate`      | Date and time the job was posted.             |

## Deployment Process

### Initial Deployment:
- Set up a Heroku account and create a new application.
- Connect the Heroku app to the GitHub repository.
- Set up automatic deployment from the main branch on Heroku.
- Configure environment variables in Heroku, such as `SECRET_KEY` and database credentials.
- Deploy the application and perform initial testing to ensure functionality.

### Ongoing Updates:
- Develop new features in separate branches in Git.
- Use pull requests to merge features into the main branch after code review.
- Continuous integration via GitHub Actions will run tests; successful results are required before merging.
- Updates are automatically deployed to Heroku when changes are merged to the main branch.

## Gathering Results

### User Feedback:
- Regularly collect user feedback through surveys and direct user communication.

### Performance Metrics:
- Monitor application performance, focusing on response times and system availability.

### Usage Statistics:
- Track active users, job postings, and search usage to assess engagement and utility.

### Maintenance and Bugs:
- Implement a system for tracking and promptly addressing bugs and maintenance issues.
