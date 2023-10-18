const mysql = require("mysql2");


// Create a connection to the database
const connection = mysql.createConnection({
  host: "database-1.c55mts1blx53.ap-south-1.rds.amazonaws.com",
  user: "root",
  password: "redhat3439",
  port: "3306",
  database: "employees_db"
});

// open the MySQL connection
connection.connect(error => {
  if (error) throw error;
  console.log("Successfully connected to the MYSQL database.");
});

module.exports = connection;
