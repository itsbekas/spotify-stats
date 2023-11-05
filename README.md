## Project Overview

**Spotify Stats** is a project designed to empower users to gain deeper insights into their Spotify data. While Spotify offers data on a user's top 50 artists and tracks over specific timeframes, **Spotify Stats** provides the freedom to analyze data in a more flexible and customizable manner. This project aims to address the limitations of Spotify's built-in data visualization by allowing users to explore their data in unique and personalized ways.

## Microservices

The architecture of **Spotify Stats** comprises the following microservices, each with distinct roles and responsibilities:

1. **REST API**
   - Serves information retrieved from a shared MongoDB database.
   - Provides an interface for clients to access and manipulate user data.

2. **Updater**
   - Retrieves data from the Spotify API and updates the shared MongoDB database.
   - Ensures data accuracy and currency by syncing with Spotify's latest insights.

3. **Importer**
   - Processes user-submitted JSON files, allowing users to import their Spotify data.
   - Writes the imported data to the shared MongoDB database, enabling users to analyze their complete listening history.

## Shared Codebase

A common codebase, managed as a package/module, is used by multiple microservices within the **Spotify Stats** architecture. This shared codebase includes database models, database access functions, and other code essential for interacting with the shared MongoDB database. It promotes code reusability, maintainability, and consistency while allowing each microservice to extend functionality according to its specific requirements.

## Database

**Spotify Stats** employs a single MongoDB database, which serves as the central data store. Multiple microservices require access to this database to retrieve, update, and import user data.

## Communication

Communication between microservices is predominantly facilitated through the use of RESTful APIs. While REST is the primary mode of communication, there are ongoing efforts to optimize and refine communication mechanisms to enhance efficiency and flexibility.

## Dependencies and Version Control

Dependencies across the microservices are managed via pip, ensuring consistent and reliable dependency resolution. Version control for both the shared codebase and the microservices themselves is accomplished using Git.

## Deployment

Docker containers are utilized for deployment, enabling efficient encapsulation of microservices and their dependencies. While Kubernetes is not currently in use, it is part of the long-term strategy to enhance orchestration and scalability.

## Testing and Quality Assurance

The project relies on pytest for testing, encompassing unit tests and ongoing quality assurance measures. The project's testing suite will continue to evolve to ensure robust functionality and data accuracy.
