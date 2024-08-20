import datetime
import os

days = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
)

months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

while True:
    print("Enter the year for the calendar:")
    response = input("> ")

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Please enter a numeric year, like 2024.")
    continue

while True:
    print("Enter the month for the calendar, 1-12:")
    response = input("> ")

    if not response.isdecimal():
        print("Please enter a numeric month, like 3 for March.")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("Please enter a numer from 1 to 12.")


def get_calendar_for(year, month):
    cal_text = ""
    cal_text += (" " * 34) + months[month - 1] + " " + str(year) + "\n"
    cal_text += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"
    week_separator = ("+----------" * 7) + "+\n"
    blank_row = ("|          " * 7) + "|\n"
    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separator
        day_number_row = ""
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += "|\n"

        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != month:
            break

    cal_text += week_separator
    return cal_text


cal_text = get_calendar_for(year, month)
print(cal_text)

downloads_path = os.path.expanduser("~/Downloads")
calendar_filename = f"calendar_{year}_{month}.txt"
full_path = os.path.join(downloads_path, calendar_filename)

with open(full_path, "w") as file_obj:
    file_obj.write(cal_text)

print(f"Saved to {full_path}")
