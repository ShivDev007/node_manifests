// const mysql = require("mysql2");


// // Create a connection to the database
// const connection = mysql.createConnection({
//   host: "database-1.c55mts1blx53.ap-south-1.rds.amazonaws.com",
//   user: "root",
//   password: "redhat3439",
//   port: "3306",
//   database: "employees_db"
// });

// // open the MySQL connection
// connection.connect(error => {
//   if (error) throw error;
//   console.log("Successfully connected to the MYSQL database.");
// });

// module.exports = connection;


// different part 
const mysql = require("mysql2");
const dotenv = require("dotenv");

dotenv.config(); // Load environment variables from .env

// Create a connection to the database
const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME
});

// Open the MySQL connection
connection.connect(error => {
  if (error) throw error;
  console.log("Successfully connected to the MySQL database.");
});

module.exports = connection;
