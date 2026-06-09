# import requests
# import os

# import zipfile
# # =========================
# # SAILPOINT DETAILS
# # =========================

# CLIENT_ID = "3e4b55c4bd0a41fba35a649141c3d848"
# CLIENT_SECRET = "6ca2c1dda414f8f50eef7495947d537b3d437f9c8b3adee5aa96fd6def3af9d9"

# BASE_URL = "https://godaddy.api.identitynow.com"

# # =========================
# # TOKEN URL
# # =========================

# TOKEN_URL = f"{BASE_URL}/oauth/token"

# # =========================
# # REPORTS FOLDER
# # =========================

# REPORT_FOLDER = "reports"

# os.makedirs(REPORT_FOLDER, exist_ok=True)

# # =========================
# # GENERATE TOKEN
# # =========================

# payload = {
#     "grant_type": "client_credentials",
#     "client_id": CLIENT_ID,
#     "client_secret": CLIENT_SECRET
# }

# print("Generating token...")

# response = requests.post(TOKEN_URL, data=payload)

# if response.status_code != 200:
#     print("Token generation failed")
#     print(response.text)
#     exit()

# token = response.json()["access_token"]

# print("Token generated successfully")

# # =========================
# # HEADERS
# # =========================

# headers = {
#     "Authorization": f"Bearer {token}"
# }

# # =========================
# # GET ALL CAMPAIGNS WITH PAGINATION
# # =========================

# print("Fetching campaigns...")

# all_campaigns = []

# offset = 0
# limit = 250

# while True:

#     campaign_url = f"{BASE_URL}/v3/campaigns?limit={limit}&offset={offset}"

#     campaign_response = requests.get(campaign_url, headers=headers)

#     if campaign_response.status_code != 200:
#         print("Failed to fetch campaigns")
#         print(campaign_response.text)
#         exit()

#     campaigns = campaign_response.json()

#     # STOP IF NO MORE CAMPAIGNS
#     if not campaigns:
#         break

#     # ADD CAMPAIGNS TO MASTER LIST
#     all_campaigns.extend(campaigns)

#     print(f"Fetched {len(campaigns)} campaigns from offset {offset}")

#     # NEXT PAGE
#     offset += limit

# # FINAL CAMPAIGNS LIST
# campaigns = all_campaigns

# print(f"Total campaigns found: {len(campaigns)}")

# # =========================
# # FILTER CAMPAIGNS
# # =========================

# FILTER_TEXT = input("Enter campaign filter text: ")
# filtered_campaigns = []

# for campaign in campaigns:

#     campaign_name = campaign.get("name", "")

#     if FILTER_TEXT in campaign_name:
#         filtered_campaigns.append(campaign)

# print(f"Matching campaigns: {len(filtered_campaigns)}")


# # =========================
# # COUNT COMPLETED CAMPAIGNS
# # =========================

# completed_campaigns = []

# for campaign in filtered_campaigns:

#     campaign_status = campaign.get("status", "").upper()

#     if campaign_status == "COMPLETED":
#         completed_campaigns.append(campaign)

# print(f"Completed campaigns: {len(completed_campaigns)}")

# # =========================
# # REPORT TYPES
# # =========================

# REPORT_TYPES = {
#     "status": "status",
#     "signoff": "signoff",
#     "composition": "composition",
#     "remediation": "remediation"
# }

# # =========================
# # DOWNLOAD REPORTS
# # =========================

# # for campaign in filtered_campaigns:

# #     campaign_id = campaign["id"]
# #     campaign_name = campaign["name"]

# #     print(f"\nProcessing campaign: {campaign_name}")

# #    # SAFE CAMPAIGN NAME
# #     safe_campaign_name = campaign_name.replace("/", "_")


# #     # CREATE CAMPAIGN FOLDER
# #     campaign_folder = os.path.join(REPORT_FOLDER, safe_campaign_name)

# #     os.makedirs(campaign_folder, exist_ok=True)

# #     # GET REPORT DETAILS
# #     report_url = f"{BASE_URL}/v3/campaigns/{campaign_id}/reports"

# #     report_response = requests.get(report_url, headers=headers)

# #     if report_response.status_code != 200:
# #         print(f"Failed fetching reports for: {campaign_name}")
# #         print(report_response.text)
# #         continue

# #     try:
# #         report_data = report_response.json()
# #     except Exception:
# #         print(f"Invalid JSON response for: {campaign_name}")
# #         continue

# #     if not report_data:
# #         print(f"No reports found for: {campaign_name}")
# #         continue








# for campaign in filtered_campaigns:

#     campaign_id = campaign["id"]
#     campaign_name = campaign["name"]

#     # =========================
#     # CHECK CAMPAIGN STATUS
#     # =========================

#     campaign_status = campaign.get("status", "").upper()

#     print(f"\nProcessing campaign: {campaign_name}")
#     print(f"Campaign Status: {campaign_status}")
#     downloaded_any_report = False

#     # DOWNLOAD ONLY COMPLETED CAMPAIGNS
#     if campaign_status != "COMPLETED":
#         print("Skipping because campaign is not COMPLETED")
#         continue

#     # =========================
#     # SAFE CAMPAIGN NAME
#     # =========================

#     safe_campaign_name = (
#     campaign_name.replace("/", "_")
#     + "_"
#     + campaign_id[:6]
# )

#     # =========================
#     # CREATE CAMPAIGN FOLDER
#     # =========================
#     campaign_folder = os.path.join(REPORT_FOLDER, safe_campaign_name)
#     # SKIP IF CAMPAIGN ALREADY DOWNLOADED
#     if os.path.exists(campaign_folder):
#          print("Campaign already downloaded. Skipping...")
#          continue

#     # Create folder only if it's a new campaign
#     os.makedirs(campaign_folder, exist_ok=True)


#     # =========================
#     # GET REPORT DETAILS
#     # =========================

#     report_url = f"{BASE_URL}/v3/campaigns/{campaign_id}/reports"

#     report_response = requests.get(report_url, headers=headers)

#     if report_response.status_code != 200:
#         print(f"Failed fetching reports for: {campaign_name}")
#         print(report_response.text)
#         continue

#     try:
#         report_data = report_response.json()
#     except Exception:
#         print(f"Invalid JSON response for: {campaign_name}")
#         continue

#     if not report_data:
#         print(f"No reports found for: {campaign_name}")
#         continue

#     # =========================
#     # PROCESS ALL REPORT TYPES
#     # =========================

#     for report in report_data:

#         report_name = report.get("name", "").lower()

#         selected_type = None

#         if "remediation status" in report_name:
#             selected_type = "remediation"
#         elif "campaign status" in report_name:
#             selected_type = "status"
#         elif "signoff" in report_name:
#              selected_type = "signoff"
#         elif "composition" in report_name:
#              selected_type = "composition"
#         if not selected_type:
#             continue

#         report_id = report.get("id")

#         if not report_id:
#             continue

#         print(f"Downloading {selected_type} report...")
#         # for getting json result of each report whether the status is success or not
#         print(report) 

#                 # =========================
#         # DOWNLOAD CSV
#         # =========================

#         csv_download_url = (
#             f"{BASE_URL}/v2025/reports/{report_id}?fileFormat=csv"
#         )

#         csv_response = requests.get(csv_download_url, headers=headers)

#         if csv_response.status_code == 200:

#             csv_file_path = os.path.join(
#                 campaign_folder,
#                 f"{selected_type}.csv"
#             )

#             with open(csv_file_path, "wb") as file:
#                 file.write(csv_response.content)

#             print(f"Saved CSV: {selected_type}.csv")
#             downloaded_any_report = True

#         else:
#             print(f"Failed CSV download for {selected_type}")
#             print(csv_response.text)

#         # =========================
#         # DOWNLOAD PDF
#         # =========================
       
#         pdf_download_url = (
#             f"{BASE_URL}/v2025/reports/{report_id}?fileFormat=pdf"
#         )

#         pdf_response = requests.get(pdf_download_url, headers=headers)

#         if pdf_response.status_code == 200:

#             pdf_file_path = os.path.join(
#                 campaign_folder,
#                 f"{selected_type}.pdf"
#             )

#             with open(pdf_file_path, "wb") as file:
#                 file.write(pdf_response.content)

#             print(f"Saved PDF: {selected_type}.pdf")
#             downloaded_any_report = True

#         else:
#             print(f"Failed PDF download for {selected_type}")
#             print(pdf_response.text)

    

#         # =========================
#     # CREATE ZIP FILE
#     # =========================

#     zip_file_path = os.path.join(
#         campaign_folder,
#         f"{safe_campaign_name}.zip"
#     )

#     with zipfile.ZipFile(zip_file_path, 'w') as zip_file:

#         for file_name in os.listdir(campaign_folder):

#             if file_name.endswith(".csv") or file_name.endswith(".pdf"):

#                 file_path = os.path.join(
#                     campaign_folder,
#                     file_name
#                 )

#                 zip_file.write(
#                     file_path,
#                     arcname=file_name
#                 )
#     print(f"Finished processing campaign: {campaign_name}")
#     print(f"ZIP created for campaign: {safe_campaign_name}.zip")
# # CREATE ZIP OF REPORTS FOLDER
# # =========================

# import shutil

# zip_file_name = "reports_backup"

# shutil.make_archive(zip_file_name, 'zip', REPORT_FOLDER)

# print(f"ZIP created successfully: {zip_file_name}.zip")

# print("\nAll processing completed .")










# import requests
# import os
# import zipfile
# import shutil

# # =========================
# # SAILPOINT DETAILS
# # =========================
# CLIENT_ID = "3e4b55c4bd0a41fba35a649141c3d848"
# CLIENT_SECRET = "6ca2c1dda414f8f50eef7495947d537b3d437f9c8b3adee5aa96fd6def3af9d9"

# BASE_URL = "https://godaddy.api.identitynow.com"

# # # =========================
# # # TOKEN URL
# # # =========================

# TOKEN_URL = f"{BASE_URL}/oauth/token"
# # =========================
# # REPORTS FOLDER
# # =========================
# REPORT_FOLDER = "reports"
# os.makedirs(REPORT_FOLDER, exist_ok=True)

# # =========================
# # GENERATE TOKEN
# # =========================
# payload = {
#     "grant_type": "client_credentials",
#     "client_id": CLIENT_ID,
#     "client_secret": CLIENT_SECRET
# }

# print("Generating token...")

# response = requests.post(TOKEN_URL, data=payload)

# if response.status_code != 200:
#     print("Token generation failed")
#     print(response.text)
#     exit()

# token = response.json()["access_token"]
# print("Token generated successfully")

# headers = {
#     "Authorization": f"Bearer {token}"
# }

# # =========================
# # FETCH CAMPAIGNS
# # =========================
# print("Fetching campaigns...")

# all_campaigns = []
# offset = 0
# limit = 250

# while True:
#     campaign_url = f"{BASE_URL}/v3/campaigns?limit={limit}&offset={offset}"

#     campaign_response = requests.get(campaign_url, headers=headers)

#     if campaign_response.status_code != 200:
#         print("Failed to fetch campaigns")
#         print(campaign_response.text)
#         exit()

#     campaigns = campaign_response.json()

#     if not campaigns:
#         break

#     all_campaigns.extend(campaigns)
#     print(f"Fetched {len(campaigns)} campaigns from offset {offset}")

#     offset += limit

# campaigns = all_campaigns
# print(f"Total campaigns found: {len(campaigns)}")

# # =========================
# # FILTER
# # =========================
# FILTER_TEXT = input("Enter campaign filter text: ")

# filtered_campaigns = [
#     c for c in campaigns if FILTER_TEXT in c.get("name", "")
# ]

# print(f"Matching campaigns: {len(filtered_campaigns)}")

# completed_campaigns = [
#     c for c in filtered_campaigns if c.get("status", "").upper() == "COMPLETED"
# ]

# print(f"Completed campaigns: {len(completed_campaigns)}")

# # =========================
# # COUNTERS
# # =========================
# downloaded_count = 0

# # =========================
# # PROCESS CAMPAIGNS (ALWAYS REFRESH)
# # =========================
# for campaign in filtered_campaigns:

#     campaign_id = campaign["id"]
#     campaign_name = campaign["name"]
#     campaign_status = campaign.get("status", "").upper()

#     print(f"\nProcessing campaign: {campaign_name}")
#     print(f"Campaign Status: {campaign_status}")

#     if campaign_status != "COMPLETED":
#         print("Skipping because campaign is not COMPLETED")
#         continue

#     safe_campaign_name = (
#         campaign_name.replace("/", "_") + "_" + campaign_id[:6]
#     )

#     campaign_folder = os.path.join(REPORT_FOLDER, safe_campaign_name)
#     os.makedirs(campaign_folder, exist_ok=True)

#     # =========================
#     # GET REPORTS
#     # =========================
#     report_url = f"{BASE_URL}/v3/campaigns/{campaign_id}/reports"

#     report_response = requests.get(report_url, headers=headers)

#     if report_response.status_code != 200:
#         print(f"Failed fetching reports for: {campaign_name}")
#         continue

#     try:
#         report_data = report_response.json()
#     except:
#         print(f"Invalid JSON response for: {campaign_name}")
#         continue

#     if not report_data:
#         print(f"No reports found for: {campaign_name}")
#         continue

#     latest_reports = {}

#     for report in report_data:

#         report_name = report.get("name", "").lower()
#         report_status = report.get("status", "").upper()
#         last_run_at = report.get("lastRunAt", "")

#         if report_status != "SUCCESS":
#             continue

#         selected_type = None

#         if "remediation status" in report_name:
#             selected_type = "remediation"
#         elif "campaign status" in report_name:
#             selected_type = "status"
#         elif "signoff" in report_name:
#             selected_type = "signoff"
#         elif "composition" in report_name:
#             selected_type = "composition"

#         if not selected_type:
#             continue

#         if (
#             selected_type not in latest_reports
#             or last_run_at > latest_reports[selected_type]["lastRunAt"]
#         ):
#             latest_reports[selected_type] = report

#     # =========================
#     # DOWNLOAD (OVERWRITE ALWAYS)
#     # =========================
#     downloaded_any = False

#     for selected_type, report in latest_reports.items():

#         report_id = report.get("id")
#         if not report_id:
#             continue

#         print(f"Downloading latest {selected_type} report...")

#         # CSV
#         csv_url = f"{BASE_URL}/v2025/reports/{report_id}?fileFormat=csv"
#         csv_response = requests.get(csv_url, headers=headers)

#         if csv_response.status_code == 200:
#             csv_path = os.path.join(campaign_folder, f"{selected_type}.csv")
#             with open(csv_path, "wb") as f:
#                 f.write(csv_response.content)
#             downloaded_any = True
#             print(f"Updated CSV: {selected_type}.csv")

#         # PDF
#         pdf_url = f"{BASE_URL}/v2025/reports/{report_id}?fileFormat=pdf"
#         pdf_response = requests.get(pdf_url, headers=headers)

#         if pdf_response.status_code == 200:
#             pdf_path = os.path.join(campaign_folder, f"{selected_type}.pdf")
#             with open(pdf_path, "wb") as f:
#                 f.write(pdf_response.content)
#             print(f"Updated PDF: {selected_type}.pdf")

#     if downloaded_any:
#         downloaded_count += 1

# # =========================
# # MASTER ZIP
# # =========================
# zip_file_name = "reports_backup"

# shutil.make_archive(zip_file_name, 'zip', REPORT_FOLDER)

# print(f"\nZIP created successfully: {zip_file_name}.zip")

# # =========================
# # SUMMARY
# # =========================
# print("\n========== FINAL SUMMARY ==========")
# print(f"Matching campaigns: {len(filtered_campaigns)}")
# print(f"Completed campaigns: {len(completed_campaigns)}")
# print(f"Updated campaigns processed: {downloaded_count}")
# print("\nAll processing completed.")

































import requests
import os
import zipfile
import shutil
from datetime import datetime

# =========================
# SAILPOINT DETAILS
# =========================
CLIENT_ID = "3e4b55c4bd0a41fba35a649141c3d848"
CLIENT_SECRET = "6ca2c1dda414f8f50eef7495947d537b3d437f9c8b3adee5aa96fd6def3af9d9"

BASE_URL = "https://godaddy.api.identitynow.com"

# # =========================
# # TOKEN URL
# # =========================

TOKEN_URL = f"{BASE_URL}/oauth/token"

# =========================
# REPORTS FOLDER
# =========================
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

# =========================
# GENERATE TOKEN
# =========================
payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}

print("Generating token...")

response = requests.post(TOKEN_URL, data=payload)

if response.status_code != 200:
    print("Token generation failed")
    print(response.text)
    exit()

token = response.json()["access_token"]

print("Token generated successfully")

# =========================
# HEADERS
# =========================
headers = {
    "Authorization": f"Bearer {token}"
}

# =========================
# FETCH CAMPAIGNS
# =========================
print("Fetching campaigns...")

all_campaigns = []

offset = 0
limit = 250

while True:

    campaign_url = (
        f"{BASE_URL}/v3/campaigns"
        f"?limit={limit}&offset={offset}"
    )

    campaign_response = requests.get(
        campaign_url,
        headers=headers
    )

    if campaign_response.status_code != 200:
        print("Failed to fetch campaigns")
        print(campaign_response.text)
        exit()

    campaigns = campaign_response.json()

    if not campaigns:
        break

    all_campaigns.extend(campaigns)

    print(f"Fetched {len(campaigns)} campaigns from offset {offset}")

    offset += limit

campaigns = all_campaigns

print(f"Total campaigns found: {len(campaigns)}")

# =========================
# FILTER CAMPAIGNS
# =========================
FILTER_TEXT = input("Enter campaign filter text: ")

filtered_campaigns = [
    c for c in campaigns
    if FILTER_TEXT in c.get("name", "")
]

print(f"Matching campaigns: {len(filtered_campaigns)}")

completed_campaigns = [
    c for c in filtered_campaigns
    if c.get("status", "").upper() == "COMPLETED"
]

print(f"Completed campaigns: {len(completed_campaigns)}")

# =========================
# COUNTERS
# =========================
downloaded_count = 0

# =========================
# PROCESS CAMPAIGNS
# =========================
for campaign in filtered_campaigns:

    campaign_id = campaign["id"]
    campaign_name = campaign["name"]

    campaign_status = campaign.get(
        "status",
        ""
    ).upper()

    print(f"\nProcessing campaign: {campaign_name}")
    print(f"Campaign Status: {campaign_status}")

    if campaign_status != "COMPLETED":
        print("Skipping because campaign is not COMPLETED")
        continue

    # =========================
    # SAFE FOLDER NAME
    # =========================
    safe_campaign_name = (
        campaign_name.replace("/", "_")
        + "_"
        + campaign_id[:6]
    )

    campaign_folder = os.path.join(
        REPORT_FOLDER,
        safe_campaign_name
    )

    os.makedirs(campaign_folder, exist_ok=True)

    # =========================
    # FETCH REPORTS
    # =========================
    report_url = (
        f"{BASE_URL}/v3/campaigns/"
        f"{campaign_id}/reports"
    )

    report_response = requests.get(
        report_url,
        headers=headers
    )

    if report_response.status_code != 200:
        print(f"Failed fetching reports for: {campaign_name}")
        print(report_response.text)
        continue

    try:
        report_data = report_response.json()

    except Exception:
        print(f"Invalid JSON response for: {campaign_name}")
        continue

    if not report_data:
        print(f"No reports found for: {campaign_name}")
        continue

    # =========================
    # PICK TRUE LATEST REPORTS
    # =========================
    latest_reports = {}

    for report in report_data:

        report_name = report.get(
            "name",
            ""
        ).lower()

        report_status = report.get(
            "status",
            ""
        ).upper()

        last_run_at = report.get(
            "lastRunAt"
        )

        if report_status != "SUCCESS":
            continue

        selected_type = None

        if "remediation status" in report_name:
            selected_type = "remediation"

        elif "campaign status" in report_name:
            selected_type = "status"

        elif "signoff" in report_name:
            selected_type = "signoff"

        elif "composition" in report_name:
            selected_type = "composition"

        if not selected_type:
            continue

        try:

            current_datetime = datetime.fromisoformat(
                last_run_at.replace("Z", "+00:00")
            )

        except Exception:
            continue

        if selected_type not in latest_reports:

            latest_reports[selected_type] = {
                "report": report,
                "datetime": current_datetime
            }

        else:

            existing_datetime = (
                latest_reports[selected_type]["datetime"]
            )

            if current_datetime > existing_datetime:

                latest_reports[selected_type] = {
                    "report": report,
                    "datetime": current_datetime
                }

    # CLEAN STRUCTURE
    latest_reports = {
        k: v["report"]
        for k, v in latest_reports.items()
    }

    # =========================
    # DOWNLOAD REPORTS
    # =========================
    downloaded_any = False

    for selected_type, report in latest_reports.items():

        report_id = report.get("id")

        if not report_id:
            continue

        print(f"Downloading latest {selected_type} report...")

        # =========================
        # CSV DOWNLOAD (STREAM MODE)
        # =========================
        csv_url = (
            f"{BASE_URL}/v2025/reports/"
            f"{report_id}?fileFormat=csv"
        )

        csv_path = os.path.join(
            campaign_folder,
            f"{selected_type}.csv"
        )

        with requests.get(
            csv_url,
            headers=headers,
            stream=True
        ) as csv_response:

            if csv_response.status_code == 200:

                with open(csv_path, "wb") as f:

                    for chunk in csv_response.iter_content(
                        chunk_size=8192
                    ):

                        if chunk:
                            f.write(chunk)

                print(f"Updated CSV: {selected_type}.csv")
                downloaded_any = True

            else:

                print(
                    f"Failed CSV download "
                    f"for {selected_type}"
                )

                print(csv_response.text)

        # =========================
        # PDF DOWNLOAD (STREAM MODE)
        # =========================
        pdf_url = (
            f"{BASE_URL}/v2025/reports/"
            f"{report_id}?fileFormat=pdf"
        )

        pdf_path = os.path.join(
            campaign_folder,
            f"{selected_type}.pdf"
        )

        with requests.get(
            pdf_url,
            headers=headers,
            stream=True
        ) as pdf_response:

            if pdf_response.status_code == 200:

                with open(pdf_path, "wb") as f:

                    for chunk in pdf_response.iter_content(
                        chunk_size=8192
                    ):

                        if chunk:
                            f.write(chunk)

                print(f"Updated PDF: {selected_type}.pdf")

            else:

                print(
                    f"Failed PDF download "
                    f"for {selected_type}"
                )

                print(pdf_response.text)

    # =========================
    # CREATE ZIP
    # =========================
    if downloaded_any:

        zip_path = os.path.join(
            campaign_folder,
            f"{safe_campaign_name}.zip"
        )

        with zipfile.ZipFile(
            zip_path,
            "w"
        ) as zip_file:

            for file_name in os.listdir(campaign_folder):

                if (
                    file_name.endswith(".csv")
                    or
                    file_name.endswith(".pdf")
                ):

                    file_path = os.path.join(
                        campaign_folder,
                        file_name
                    )

                    zip_file.write(
                        file_path,
                        arcname=file_name
                    )

        print(f"ZIP created: {zip_path}")

        downloaded_count += 1

# =========================
# MASTER ZIP
# =========================
zip_file_name = "reports_backup"

shutil.make_archive(
    zip_file_name,
    'zip',
    REPORT_FOLDER
)

print(
    f"\nZIP created successfully: "
    f"{zip_file_name}.zip"
)

# =========================
# FINAL SUMMARY
# =========================
print("\n========== FINAL SUMMARY ==========")

print(
    f"Matching campaigns: "
    f"{len(filtered_campaigns)}"
)

print(
    f"Completed campaigns: "
    f"{len(completed_campaigns)}"
)

print(
    f"Updated campaigns processed: "
    f"{downloaded_count}"
)

print("\nAll processing completed.")