# Star Wars API

## Project Description
The Star Wars API project is a Node.js script that interacts with the Star Wars API (SWAPI) to fetch and display character names from a specific Star Wars movie. By providing the movie ID as a command line argument, the script will print each character's name line by line in the order they appear in the movie's "characters" list.

## Installation Instructions
To set up and run the Star Wars API project, follow these steps:

### 1. Clone the repository:

```sh
git clone https://github.com/skyino7/alx-interview/0x06-starwars_api.git
cd 0x06-starwars_api
```

### 2. Install the required dependencies:
Ensure you have Node.js installed. Then, install the request module:

```sh
npm install request
```

### 3. Save the script:
Save the provided script to a file named starwars_characters.js in the project directory.

## Usage Instructions
To use the script, follow these steps:

1. Open your terminal and navigate to the project directory.
1. Run the script with the movie ID as a positional argument. For example, to get the characters from "Return of the Jedi" (which has an ID of 3), use the following command:

```sh
node starwars_characters.js 3
```
Replace **3** with the desired movie ID to fetch characters from a different Star Wars movie.

### Contributing Guidelines
We welcome contributions to the Star Wars API project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License Information
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.

By using the Star Wars API project, you agree to abide by the terms and conditions outlined in the license. If you have any questions or need further assistance, feel free to open an issue in the repository. May the Force be with you!