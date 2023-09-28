import subprocess
import random

indian_names = [
    "Aarav", "Abhinav", "Aditi", "Akshay", "Alok", "Amara", "Anaya", "Aniket", "Anisha", "Anjali",
    "Ansh", "Aryan", "Asha", "Asher", "Ayush", "Bhavya", "Chetan", "Disha", "Divya", "Eesha",
    "Ekta", "Firoz", "Gaurav", "Gopal", "Harsha", "Ishaan", "Janaki", "Karan", "Kavya", "Krish",
    "Lakshmi", "Mahi", "Manish", "Meera", "Mohit", "Neha", "Nikita", "Nishant", "Pooja", "Pranav",
    "Priya", "Rahul", "Raj", "Rani", "Rishi", "Riya", "Rohan", "Ruchi", "Sachin", "Sakshi",
    "Sameer", "Sanaya", "Sandeep", "Sarika", "Shiv", "Shruti", "Siddharth", "Simran", "Sohan", "Sonal",
    "Sonia", "Sumit", "Sunita", "Suraj", "Tanvi", "Tanya", "Tarun", "Ujjwal", "Varun", "Vicky",
    "Vidya", "Vikas", "Vishal", "Yash", "Zara", "Abha", "Abhishek", "Aditya", "Alisha", "Amar",
    "Anamika", "Anjana", "Ankit", "Anshul", "Archana", "Arjun", "Ayesha", "Chandan", "Charu", "Deepak",
    "Ekta", "Gagan", "Gauri", "Geeta", "Gunjan", "Harsh", "Hema", "Himanshu", "Indira", "Jai",
    "Juhi", "Kanchan", "Kapil", "Kavita", "Khushi", "Kirti", "Kunal", "Leela", "Madhu", "Manoj",
    "Meenakshi", "Meera", "Mira", "Mukesh", "Naveen", "Nisha", "Nitesh", "Pallavi", "Pankaj", "Payal",
    "Priyanka", "Puneet", "Radha", "Raghav", "Rajan", "Rekha", "Riya", "Rupali", "Sagar", "Samir",
    "Shalini", "Shashi", "Shikha", "Shivani", "Shubham", "Siddhi", "Sneha", "Sonam", "Sonu", "Suman",
    "Sunil", "Suresh", "Sushma"
]



def generate_phone_number():
    number = "9"  # Indian mobile numbers typically start with 9
    for _ in range(9):
        number += str(random.randint(0, 9))
    return number

# Generate a list of 500 random phone numbers
indian_phone_numbers = [generate_phone_number() for _ in range(len(indian_names))]


indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Lucknow",
    "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", "Srinagar",
    "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Ranchi", "Haora", "Coimbatore", "Jabalpur", "Gwalior",
    "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Chandigarh", "Guwahati", "Solapur", "Hubli-Dharwad", "Bareilly"
]


# Loop through the range of Indian names
for emp_name in indian_names:
    # Randomly select an Indian city and phone number
    emp_city = random.choice(indian_cities)
    emp_contact = generate_phone_number()

    curl_command = [
    "curl",
    "-X", "POST",
    "-d", f"emp_name={emp_name}&emp_contact={emp_contact}&emp_add={emp_city}",
    "http://65.2.127.229:32000/addData"]
    # Run the curl command and capture the output
    try:
        result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # Access the result.stdout to get the command output
        print("Command Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        # Handle errors, if any
        print("Error:", e)