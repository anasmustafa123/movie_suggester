# [MtvInsight]()  

[![image 1](./images/img1.png)]
[![image 2](./images/img2.png)]

## Description
MtvInsight is a movie and TV shows prediction website that leverages a dataset comprising 10k movies and 11k TV shows manually collected from [The Movie Database](https://developer.themoviedb.org/docs/getting-started). The prediction process involves converting each movie or TV show into a vector and determining their similarity based on the direction of these vectors. A small angle between vectors indicates similarity in content.

## Inspiration
I wanted to make a project that i can use and also use machinelearning init

## Quick Start
- [MtvInsight](https://movie-suggester-dun.vercel.app) 

### Install Locally
-
#### Backend Installation:
```bash
# Move to the backend directory
cd backend

# Install Python dependencies using pip
pip install -r requirements.txt
```
#### Run Backend Server
```bash
# Start the Flask server in development mode
flask run
```
#### Frontend Installation:
```bash
# Move to the frontend directory
cd frontend

# Install Node.js dependencies using npm
npm install
```
#### Run Frontend Server locally
```bash
#run the server in development
npm run dev
```

## Usage
- dataset
    option 1: installing manually using [tmdbapi]() ==Warning== it takes alot of time to fetch all the data manually.
    code for fetching the movies, tvshow data from []()
    code for preparing and processing the similarities in jupiter notebook [movie](), [shows]()

    option 2: you can access the the dataset directly from [tmdb]() dataset a collection of 5k movies
    code for preparing and processing the similarities in jupiter notebook [movie]() [shows]()
- doployment 
>   frontend(react)   --> [vercel](https://vercel.com/)
>   backend(flask)    --> [google-cloud](https://console.cloud.google.com)
>   database(mongodb) --> [atlas](https://www.mongodb.com/atlas/database)

- loading svgs
>   i used the cool library [react-loader-spinner](https://www.npmjs.com/package/react-loader-spinner)


## stack 
> backend
- flask
> frontend
- react
- vanilla css

## Contributing
