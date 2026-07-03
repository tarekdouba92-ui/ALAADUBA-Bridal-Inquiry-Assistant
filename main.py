import csv
import os
from datetime import datetime

def generate_reply(client_name, country, dress_type, inquiry_type):
    if inquiry_type == "1":
        reply = f"""
Dear {client_name},

Thank you for reaching out to ALAADUBA.

We would be honored to assist you with your {dress_type} inquiry.
Since you are contacting us from {country}, we can guide you through the process clearly and professionally.

To begin, we would love to understand your wedding date, preferred style, and whether you are looking for a custom-made or ready-to-wear piece.

Warm regards,
ALAADUBA Team
"""

    elif inquiry_type == "2":
        reply = f"""
Dear {client_name},

Thank you for your interest in ALAADUBA.

Regarding pricing, each {dress_type} is priced according to the design, materials, handwork, and level of customization required.

Once we understand your preferred direction, timeline, and details, we can guide you with a more accurate quotation.

Warm regards,
ALAADUBA Team
"""

    elif inquiry_type == "3":
        reply = f"""
Dear {client_name},

Thank you for contacting ALAADUBA.

We would be happy to assist you with arranging an appointment.
Please share your preferred date, available time, and whether your visit is for bridal, evening wear, or a custom-made consultation.

Warm regards,
ALAADUBA Team
"""

    else:
        reply = f"""
Dear {client_name},

Thank you for reaching out to ALAADUBA.

We would be happy to assist you. Please share more details about your inquiry so our team can guide you properly.

Warm regards,
ALAADUBA Team
"""

    return reply

def save_client(client_name, phone, country, dress_type, wedding_date, language, inquiry_type, status, reply):
    file_name = "clients.csv"
    file_exists = os.path.exists(file_name)

    clean_reply = " ".join(reply.split())

    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Client Name",
                "Phone",
                "Country",
                "Dress Type",
                "Wedding Date",
                "Language",
                "Inquiry Type",
                "Status",
                "Reply"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            client_name,
            phone,
            country,
            dress_type,
            wedding_date,
            language,
            inquiry_type,
            status,
            clean_reply
        ])

def create_new_inquiry():
    client_name = input("Client name: ")
    phone = input("Client phone: ")
    country = input("Client country: ")
    dress_type = input("Dress type: ")
    wedding_date = input("Wedding date: ")
    language = input("Language English/Arabic: ").lower().strip()

    print("\nChoose inquiry type:")
    print("1 - New bridal inquiry")
    print("2 - Price request")
    print("3 - Appointment request")

    inquiry_type = input("Enter number: ")

    inquiry_labels = {
        "1": "New bridal inquiry",
        "2": "Price request",
        "3": "Appointment request"
    }

    inquiry_label = inquiry_labels.get(inquiry_type, "General inquiry")

    status_labels = {
        "1": "Waiting for details",
        "2": "Price requested",
        "3": "Appointment requested"
    }

    status = status_labels.get(inquiry_type, "New inquiry")


    reply = generate_reply(client_name, country, dress_type, inquiry_type)

    print(reply)

    with open("reply.txt", "w", encoding="utf-8") as file:
        file.write(reply)

    save_client(client_name, phone, country, dress_type, wedding_date, language, inquiry_label, status, reply)

    print("Client saved successfully.")

def view_saved_clients():
    file_name = "clients.csv"

    if not os.path.exists(file_name):
        print("No clients saved yet.")
        return

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("\nSaved Clients:")

        for index, row in enumerate(reader, start=1):
            print(f"""
Client #{index}
Name: {row["Client Name"]}
Phone: {row["Phone"]}
Country: {row["Country"]}
Dress Type: {row["Dress Type"]}
Wedding Date: {row["Wedding Date"]}
Inquiry Type: {row["Inquiry Type"]}
Status: {row["Status"]}
""")
            
def search_client():
    file_name = "clients.csv"

    if not os.path.exists(file_name):
        print("No clients saved yet.")
        return

    search_term = input("Enter client name or phone: ").lower().strip()
    found = False

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for index, row in enumerate(reader, start=1):
            client_name = row["Client Name"].lower()
            phone = row["Phone"].lower()

            if search_term in client_name or search_term in phone:
                found = True
                print(f"""
Client #{index}
Name: {row["Client Name"]}
Phone: {row["Phone"]}
Country: {row["Country"]}
Dress Type: {row["Dress Type"]}
Wedding Date: {row["Wedding Date"]}
Inquiry Type: {row["Inquiry Type"]}
Status: {row["Status"]}
""")

    if not found:
        print("No matching client found.")

while True:
    print("\nWelcome to ALAADUBA Bridal Assistant")
    print("1 - Create new inquiry")
    print("2 - View saved clients")
    print("3 - Search client")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_new_inquiry()

    elif choice == "2":
        view_saved_clients()

    elif choice == "3":
        search_client()

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
