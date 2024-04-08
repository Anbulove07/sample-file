import requests
import json
import openpyxl


def api_for_iCompare():
    # Define the API endpoint URL

    # Define the API endpoint URL
    url = "http://172.16.200.157/api/comparison/compare"

    # Define the JSON data to be sent in the POST request
    data = {
        "file1": {
            "url": "http://issez-s163/anbu/uploads/64e86750d0414/file1.pdf"
        },
        "file2": {
            "url": "http://issez-s163/anbu/uploads/64e86750d0414/file2.pdf"
        },
        "name": "My Comparison",
        "result": "pdf"
    }

    # Define your Basic Auth credentials
    username = "iCompare"
    password = "iCompare"

    # Send the POST request with JSON data and Basic Authentication headers
    response = requests.post(url, json=data, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # # Parse the JSON response
        # response_data = response.json()
        #
        # # Print the response
        # print("Response:")
        # print(json.dumps(response_data, indent=4))
        response_data = response.content  # Get the response content (PDF bytes)

        # Save the response PDF to a file
        with open("D:\Giventool\karthik\IOPP\IOPP\Input\TRAN_114304\Source\out.pdf", 'wb') as output_file:
            output_file.write(response_data)
    else:
        print(f"Error: {response.status_code} - {response.text}")


    # Load your JSON data
    data  = response_data
    if len(data['differences']) == 0:
        return "True"

    wb = openpyxl.Workbook()
    ws = wb.active

    # Write header row
    header = ["Document", "CompareDocument", "PageNumber", "ModificationType", "MediaType", "Message"]
    ws.append(header)
    # Write data rows
    for diff in data['differences']:
        row = [data['document'], data['compareDocument'], diff['pageNumber'], diff['modificationType'], diff['mediaType'], diff['message']]
        ws.append(row)

    # Save the workbook to a file
    wb.save("comparison_report.xlsx")
    return "False"

api_for_iCompare()